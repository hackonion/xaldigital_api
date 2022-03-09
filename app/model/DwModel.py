"""
- Data classes for the DWModel application
"""
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class Dw(db.Model):
    id: int
    first_name: str
    last_name: str
    company_name: str
    address: str
    city: str
    state: str
    zip: int
    phone1: str
    phone2: str
    email: str
    department: str

    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    company_name = db.Column(db.String(50),nullable=True)
    address = db.Column(db.String(50),nullable=True)
    city = db.Column(db.String(50),nullable=True)
    state = db.Column(db.String(50),nullable=True)
    zip = db.Column(db.Integer,nullable=True)
    phone1 = db.Column(db.String(20),nullable=False)
    phone2 = db.Column(db.String(20),nullable=True)
    email = db.Column(db.String(50),nullable=False)
    department = db.Column(db.String(50),nullable=True)
