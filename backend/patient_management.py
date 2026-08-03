# ClinRx-ICU-CCU Patient Management Module

patients = []


def add_patient(patient_data):
    patients.append(patient_data)
    return {
        "status": "success",
        "message": "Patient added successfully"
    }


def get_patients():
    return patients


def get_patient(patient_id):

    for patient in patients:
        if patient.get("patient_id") == patient_id:
            return patient

    return {
        "message": "Patient not found"
    }
