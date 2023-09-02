from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List
import random

correct_username = "user"
correct_password = "user"
app = FastAPI()

Base = declarative_base()

DATABASE_URL = "postgresql://user:user@db:5432/contacts_base"
#DATABASE_URL = "postgresql://user:user@localhost:5432/contacts_base"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    names = Column(String)
    phone = Column(String)
    email = Column(String)


class ContactCreate(BaseModel):
    names: str
    phone: str
    email: str


class ContactInfo(BaseModel):
    id: int
    names: str
    phone: str
    email: str


class ContactUpdate(BaseModel):
    names: str
    phone: str
    email: str


security = HTTPBasic()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/contacts/")
def create_contact(contact: ContactCreate, credentials: HTTPBasicCredentials = Depends(security), db=Depends(get_db)):

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Неправильные учетные данные")
    idi = random.randint(0, 999999999)
    new_contact = Contact(id=idi, names=contact.names, phone=contact.phone, email=contact.email)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"message": "Контакт успешно создан", "contact_id": new_contact.id}


@app.get("/contacts/{contact_id}", response_model=ContactInfo)
def get_contact(contact_id: int, credentials: HTTPBasicCredentials = Depends(security), db=Depends(get_db)):
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Неправильные учетные данные")

    contact = db.query(Contact).filter(Contact.id == contact_id).first()

    if not contact:
        raise HTTPException(status_code=404, detail="Контакт не найден")

    return ContactInfo(id=contact.id, names=contact.names, phone=contact.phone, email=contact.email)


@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, credentials: HTTPBasicCredentials = Depends(security), db=Depends(get_db)):
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Неправильные учетные данные")

    contact = db.query(Contact).filter(Contact.id == contact_id).first()

    if not contact:
        raise HTTPException(status_code=404, detail="Контакт не найден")

    db.delete(contact)
    db.commit()

    return {"message": "Контакт успешно удален"}


@app.put("/contacts/{contact_id}", response_model=ContactInfo)
def update_contact(
        contact_id: int,
        contact_update: ContactUpdate,
        credentials: HTTPBasicCredentials = Depends(security),
        db=Depends(get_db)):
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Неправильные учетные данные")

    contact = db.query(Contact).filter(Contact.id == contact_id).first()

    if not contact:
        raise HTTPException(status_code=404, detail="Контакт не найден")

    contact.names = contact_update.names
    contact.phone = contact_update.phone
    contact.email = contact_update.email

    db.commit()
    db.refresh(contact)

    return ContactInfo(id=contact.id, names=contact.names, phone=contact.phone, email=contact.email)


@app.get("/contacts", response_model=List)
def get_contact(credentials: HTTPBasicCredentials = Depends(security), db=Depends(get_db)):
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Неправильные учетные данные")

    contact = db.query(Contact).all()

    if not contact:
        raise HTTPException(status_code=404, detail="Контакт не найден")

    return contact
