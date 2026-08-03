# ClinRx-ICU-CCU Clinical Report Generator

def generate_report(patient, medications, alerts, interventions):

    report = {
        "Patient Information": patient,
        "Medication Review": medications,
        "Clinical Alerts": alerts,
        "Pharmacist Interventions": interventions
    }

    return report
