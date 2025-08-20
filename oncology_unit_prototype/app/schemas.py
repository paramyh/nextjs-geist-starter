from datetime import date
from typing import Optional, List
from pydantic import BaseModel

class PatientBase(BaseModel):
    national_id: Optional[str] = None
    hospital_id: str
    first_name: str
    last_name: str
    gender: str
    dob: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    next_of_kin: Optional[str] = None
    allergies: Optional[str] = None
    status: Optional[str] = "Active"

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    class Config:
        from_attributes = True

class DiagnosisBase(BaseModel):
    patient_id: int
    icd10_code: str
    cancer_site: str
    stage: Optional[str] = None
    grade: Optional[str] = None
    histology: Optional[str] = None
    notes: Optional[str] = None
    date_diagnosed: Optional[date] = None

class DiagnosisCreate(DiagnosisBase):
    pass

class Diagnosis(DiagnosisBase):
    id: int
    class Config:
        from_attributes = True

class RegimenBase(BaseModel):
    name: str
    description: Optional[str] = None
    cycle_length_days: Optional[int] = None
    total_cycles: Optional[int] = None

class RegimenCreate(RegimenBase):
    pass

class Regimen(RegimenBase):
    id: int
    class Config:
        from_attributes = True

class MedicationBase(BaseModel):
    name: str
    atc_code: Optional[str] = None
    route: Optional[str] = None
    strength: Optional[str] = None
    is_supportive: Optional[bool] = False

class MedicationCreate(MedicationBase):
    pass

class Medication(MedicationBase):
    id: int
    class Config:
        from_attributes = True

class InventoryBase(BaseModel):
    medication_id: int
    batch_no: str
    quantity: float
    unit: Optional[str] = None
    expiry_date: Optional[date] = None

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int
    class Config:
        from_attributes = True

class AppointmentBase(BaseModel):
    patient_id: int
    date: date
    purpose: str
    clinician: Optional[str] = None
    status: Optional[str] = "Booked"

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    class Config:
        from_attributes = True

class PrescriptionItemBase(BaseModel):
    medication_id: int
    dose: str
    frequency: Optional[str] = None
    route: Optional[str] = None
    notes: Optional[str] = None

class PrescriptionItemCreate(PrescriptionItemBase):
    pass

class PrescriptionItem(PrescriptionItemBase):
    id: int
    class Config:
        from_attributes = True

class PrescriptionBase(BaseModel):
    patient_id: int
    regimen_id: Optional[int] = None
    date_prescribed: date
    cycle_no: Optional[int] = None
    notes: Optional[str] = None

class PrescriptionCreate(PrescriptionBase):
    items: List[PrescriptionItemCreate] = []

class Prescription(PrescriptionBase):
    id: int
    items: List[PrescriptionItem] = []
    class Config:
        from_attributes = True

class VisitBase(BaseModel):
    patient_id: int
    date: date
    clinician: Optional[str] = None
    complaints: Optional[str] = None
    investigations: Optional[str] = None
    plan: Optional[str] = None
    next_appointment_date: Optional[date] = None

class VisitCreate(VisitBase):
    pass

class Visit(VisitBase):
    id: int
    class Config:
        from_attributes = True
