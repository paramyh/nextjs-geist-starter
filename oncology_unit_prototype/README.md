# Oncology Unit Management - Working Prototype (FastAPI)

This is a **backend working prototype** for an Oncology Unit Management System with a redundancy-free relational design.
It includes:
- FastAPI + SQLite (SQLAlchemy) with models for Patients, Cancer Diagnoses, Appointments, Prescriptions, Regimens, Inventory, and Visits.
- Built-in interactive API docs at `/docs` (Swagger UI).
- SQL schema (`schema.sql`) for reference or initializing a database.
- Database design document (`Database_Design.docx`).
- Sample Word forms in `sample_forms/` folder.

## Quick Start

1. Create a Python virtual environment and install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API:
```bash
uvicorn app.main:app --reload
```

3. Open your browser:
```
http://127.0.0.1:8000/docs
```

4. Create initial data using the endpoints:
- `POST /patients/`
- `POST /regimens/`
- `POST /medications/`
- `POST /inventory/`
- `POST /diagnoses/`
- `POST /appointments/`
- `POST /prescriptions/`
- `POST /visits/`

## Notes
- The app uses a local SQLite database (`oncology.db`) in the project root by default.
- Authentication is kept simple for prototype purposes. Add auth/roles before production.
- The database is normalized to avoid redundancy (unique IDs, FKs, indexes).
