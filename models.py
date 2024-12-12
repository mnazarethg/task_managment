import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from datetime import datetime

engine = create_engine(f'postgresql://admin:admin@localhost:5433/practica-1')
Session = sessionmaker(bind=engine)
session = Session()

print(session)

Base = declarative_base()

class Task(Base):
    print("pasa por la funcion")
    __tablename__ = 'task' 
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    completed = Column(Boolean, default=False)
    date = Column(DateTime, default=datetime.now)
    print(Base)

Base.metadata.create_all(engine)

print("Terminó el script")
