-- Oncology Unit Management SQL Schema (SQLite dialect)

CREATE TABLE IF NOT EXISTS patients (
  id INTEGER PRIMARY KEY,
  national_id TEXT UNIQUE,
  hospital_id TEXT UNIQUE NOT NULL,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  gender TEXT NOT NULL,
  dob DATE,
  phone TEXT,
  email TEXT,
  next_of_kin TEXT,
  allergies TEXT,
  status TEXT DEFAULT 'Active'
);

CREATE TABLE IF NOT EXISTS diagnoses (
  id INTEGER PRIMARY KEY,
  patient_id INTEGER NOT NULL,
  icd10_code TEXT NOT NULL,
  cancer_site TEXT NOT NULL,
  stage TEXT,
  grade TEXT,
  histology TEXT,
  notes TEXT,
  date_diagnosed DATE,
  FOREIGN KEY(patient_id) REFERENCES patients(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS regimens (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  description TEXT,
  cycle_length_days INTEGER,
  total_cycles INTEGER
);

CREATE TABLE IF NOT EXISTS medications (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  atc_code TEXT,
  route TEXT,
  strength TEXT,
  is_supportive INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS inventory (
  id INTEGER PRIMARY KEY,
  medication_id INTEGER NOT NULL,
  batch_no TEXT NOT NULL,
  quantity REAL NOT NULL,
  unit TEXT,
  expiry_date DATE,
  UNIQUE(medication_id, batch_no),
  FOREIGN KEY(medication_id) REFERENCES medications(id)
);

CREATE TABLE IF NOT EXISTS appointments (
  id INTEGER PRIMARY KEY,
  patient_id INTEGER NOT NULL,
  date DATE NOT NULL,
  purpose TEXT NOT NULL,
  clinician TEXT,
  status TEXT DEFAULT 'Booked',
  FOREIGN KEY(patient_id) REFERENCES patients(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS prescriptions (
  id INTEGER PRIMARY KEY,
  patient_id INTEGER NOT NULL,
  regimen_id INTEGER,
  date_prescribed DATE NOT NULL,
  cycle_no INTEGER,
  notes TEXT,
  FOREIGN KEY(patient_id) REFERENCES patients(id) ON DELETE CASCADE,
  FOREIGN KEY(regimen_id) REFERENCES regimens(id)
);

CREATE TABLE IF NOT EXISTS prescription_items (
  id INTEGER PRIMARY KEY,
  prescription_id INTEGER NOT NULL,
  medication_id INTEGER NOT NULL,
  dose TEXT NOT NULL,
  frequency TEXT,
  route TEXT,
  notes TEXT,
  FOREIGN KEY(prescription_id) REFERENCES prescriptions(id) ON DELETE CASCADE,
  FOREIGN KEY(medication_id) REFERENCES medications(id)
);

CREATE TABLE IF NOT EXISTS visits (
  id INTEGER PRIMARY KEY,
  patient_id INTEGER NOT NULL,
  date DATE NOT NULL,
  clinician TEXT,
  complaints TEXT,
  investigations TEXT,
  plan TEXT,
  next_appointment_date DATE,
  FOREIGN KEY(patient_id) REFERENCES patients(id) ON DELETE CASCADE
);
