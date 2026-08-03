# ClinRx-ICU-CCU Medication Management Module

medications = []


def add_medication(medication_data):
    medications.append(medication_data)

    return {
        "status": "success",
        "message": "Medication added successfully"
    }


def get_medications():
    return medications


def search_medication(drug_name):

    results = []

    for medication in medications:
        if medication.get("drug_name", "").lower() == drug_name.lower():
            results.append(medication)

    return results
