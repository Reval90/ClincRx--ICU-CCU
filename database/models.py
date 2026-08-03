from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    patient_id = Column(String)
    age = Column(Integer)
    gender = Column(String)
    weight = Column(Float)
    diagnosis = Column(String)


class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True)
    drug_name = Column(String)
    dose = Column(String)
    route = Column(String)
    indication = Column(String)
