from sqlalchemy.orm import sessionmaker
import json 
import streamlit as st
from models import engine, Task

Session = sessionmaker(bind=engine)

def add_task():
    task_title = st.text_input("Título: ", " ")
    task_description = st.text_input("Descripción: ", " ")
    
    if st.button("Agregar"):
        try:
            new_task = Task(title=task_title, description=task_description)
            session = Session()
            session.add(new_task)
            session.commit()
            session.close()
        except Exception as e:
            st.error(f"Error al agregar la tarea: {str(e)}")
            
def list_task():
    try:
        session = Session()
        tasks = session.query(Task).all()
        for i, task in enumerate(tasks):
            st.write(f"- {task.title}: {task.description}")
            completed_task(task, session, key=f"completed_{task.id}")
            delete_task(task, session, key=f"delete_{task.id}")
        session.close()
    except Exception as e:
        st.error(f"Error al listar las tareas: {str(e)}")

def completed_task(task, session, key):
    if st.checkbox(f"Completada", value=task.completed, key=key):
        try:
            task.completed = True
            session.commit()
        except Exception as e:
            st.error(f"Error al marcar la tarea como completada: {str(e)}")

def delete_task(task, session, key):
    if task.completed and st.button(f"Eliminar", key=key):
        try:
            session.delete(task)
            session.commit()
        except Exception as e:
            st.error(f"Error al eliminar la tarea: {str(e)}")


def import_export():
    #Import
    session = Session()
    uploaded_file = st.file_uploader("Importar tareas desde un archivo", type=["json"])
    if uploaded_file is not None:
        try:
            tasks_data = json.load(uploaded_file)
            for task_data in tasks_data:
                new_task = Task(
                    title=task_data["title"],
                    description=task_data["description"],
                    completed=task_data["completed"]
                )
                session.add(new_task)
            session.commit()
        except Exception as e:
            st.error(f"Error al importar tareas: {str(e)}")
    
    #Export
    try:
        tasks = session.query(Task).all()
        tasks_data = [
            {
                "title": task.title,
                "description": task.description,
                "completed": task.completed
            }
            for task in tasks
        ]
        tasks_json = json.dumps(tasks_data)
        st.download_button(
            label="Exportar",
            data=tasks_json,
            file_name="tasks.json",
            mime="application/json"
        )
        session.close()
    except Exception as e:
            st.error(f"Error al exportar las tareas: {str(e)}")
        
        

