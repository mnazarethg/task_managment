import streamlit as st
import managment 

st.title("Gestor de Tareas")

managment.import_export()
managment.add_task()
managment.list_task()