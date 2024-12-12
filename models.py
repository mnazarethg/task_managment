from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

print(session)

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task' 
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500))
    completed = Column(Boolean, default=False)
    date = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)
