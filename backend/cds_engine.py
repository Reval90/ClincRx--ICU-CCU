# ClinRx-ICU-CCU Clinical Decision Support Main Engine

from clinical_alerts import check_laboratory_alerts, check_vital_sign_alerts
from drug_interaction import check_interactions
from dose_adjustment import renal_dose_check


def run_clinical_review(patient):

    results = {}

    results["lab_alerts"] = check_laboratory_alerts(
        patient.get("labs", {})
    )

    results["vital_alerts"] = check_vital_sign_alerts(
        patient.get("vitals", {})
    )

    results["drug_interactions"] = check_interactions(
        patient.get("medications", [])
    )

    results["dose_review"] = renal_dose_check(
        patient.get("creatinine_clearance", 100),
        patient.get("medication", "")
    )

    return results
