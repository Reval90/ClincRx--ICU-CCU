# ClinRx-ICU-CCU Medication Reconciliation Module

def compare_medication_lists(home_meds, hospital_meds):

    discrepancies = []

    for drug in home_meds:
        if drug not in hospital_meds:
            discrepancies.append({
                "drug": drug,
                "issue": "Medication not continued",
                "action": "Review clinical necessity"
            })

    for drug in hospital_meds:
        if drug not in home_meds:
            discrepancies.append({
                "drug": drug,
                "issue": "New medication started",
                "action": "Verify indication"
            })

    return discrepancies
