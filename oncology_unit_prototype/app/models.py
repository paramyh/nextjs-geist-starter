from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Text, UniqueConstraint, DateTime, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    national_id = Column(String, unique=True, index=True, nullable=True)
    hospital_id = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    dob = Column(Date, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    next_of_kin = Column(String, nullable=True)
    allergies = Column(Text, nullable=True)
    status = Column(String, default="Active")  # Active, Remission, Palliative, Discharged

    diagnoses = relationship("Diagnosis", back_populates="patient", cascade="all, delete")
    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete")
    prescriptions = relationship("Prescription", back_populates="patient", cascade="all, delete")
    visits = relationship("Visit", back_populates="patient", cascade="all, delete")

class Diagnosis(Base):
    __tablename__ = "diagnoses"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)
    icd10_code = Column(String, nullable=False, index=True)
    cancer_site = Column(String, nullable=False)  # e.g., Breast, Colon
    stage = Column(String, nullable=True)         # TNM or stage I-IV
    grade = Column(String, nullable=True)
    histology = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    date_diagnosed = Column(Date, nullable=True)

    patient = relationship("Patient", back_populates="diagnoses")

class Regimen(Base):
    __tablename__ = "regimens"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)          # e.g., FOLFOX, CHOP
    description = Column(Text, nullable=True)
    cycle_length_days = Column(Integer, nullable=True)          # e.g., 14, 21
    total_cycles = Column(Integer, nullable=True)

class Medication(Base):
    __tablename__ = "medications"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    atc_code = Column(String, nullable=True, index=True)
    route = Column(String, nullable=True)           # IV, PO, SC, etc.
    strength = Column(String, nullable=True)        # 500mg/vial, etc.
    is_supportive = Column(Boolean, default=False)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    medication_id = Column(Integer, ForeignKey("medications.id"), nullable=False, index=True)
    batch_no = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)        # units/vials
    unit = Column(String, nullable=True)
    expiry_date = Column(Date, nullable=True)

    medication = relationship("Medication")

    __table_args__ = (UniqueConstraint('medication_id', 'batch_no', name='uix_med_batch'),)

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    purpose = Column(String, nullable=False)   # New, Follow-up, Chemo, Radiotherapy, Pharmacy
    clinician = Column(String, nullable=True)
    status = Column(String, default="Booked")  # Booked, Completed, No-Show, Cancelled

    patient = relationship("Patient", back_populates="appointments")

class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)
    regimen_id = Column(Integer, ForeignKey("regimens.id"), nullable=True, index=True)
    date_prescribed = Column(Date, nullable=False)
    cycle_no = Column(Integer, nullable=True)
    notes = Column(Text, nullable=True)

    patient = relationship("Patient", back_populates="prescriptions")
    regimen = relationship("Regimen")
    items = relationship("PrescriptionItem", back_populates="prescription", cascade="all, delete")

class PrescriptionItem(Base):
    __tablename__ = "prescription_items"
    id = Column(Integer, primary_key=True, index=True)
    prescription_id = Column(Integer, ForeignKey("prescriptions.id"), nullable=False, index=True)
    medication_id = Column(Integer, ForeignKey("medications.id"), nullable=False, index=True)
    dose = Column(String, nullable=False)        # e.g., 85 mg/m^2
    frequency = Column(String, nullable=True)    # e.g., day 1, days 1-5
    route = Column(String, nullable=True)
    notes = Column(Text, nullable=True)

    prescription = relationship("Prescription", back_populates="items")
    medication = relationship("Medication")

class Visit(Base):
    __tablename__ = "visits"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False, index=True)
    date = Column(Date, nullable=False)
    clinician = Column(String, nullable=True)
    complaints = Column(Text, nullable=True)
    investigations = Column(Text, nullable=True)
    plan = Column(Text, nullable=True)
    next_appointment_date = Column(Date, nullable=True)

    patient = relationship("Patient", back_populates="visits")
