from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from datetime import datetime

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'
    
    email = Column(String, primary_key=True,nullable=False)
    student_id = Column(Integer, nullable=False)
    password = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    classes = Column(String)
    role = Column(String, nullable=False)

class ClassModel(Base):
    __tablename__ = 'class'

    class_code = Column(Integer, primary_key=True,nullable=False)
    name = Column(String, nullable= False)
    links = Column(String)

class  MessageModel(Base):
    __tablename__ = 'message'

    student_id = Column(Integer,primary_key=True, nullable=False)
    class_code = Column(Integer,nullable=False)
    content = Column(String)
    created_by = Column(DateTime, default= datetime.utcnow)

class NoteModel(Base):
    __tablename__ = 'note'

    note_id = Column(Integer, primary_key=True, nullable=False)
    student_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    class_code = Column(Integer,nullable=False)
    created_by = Column(DateTime, default= datetime.utcnow)

class tagModel(Base):
    __tablename__ = 'tags'

    name = Column(String, nullable=False,primary_key=True)
    class_code = Column(Integer,nullable=False)



