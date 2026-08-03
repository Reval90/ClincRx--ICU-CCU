# ClinRx-ICU-CCU ICU Scoring Support Module

def calculate_sofa_components(data):

    score = {}

    score["respiratory"] = data.get("respiratory_score", 0)
    score["coagulation"] = data.get("platelet_score", 0)
    score["liver"] = data.get("bilirubin_score", 0)
    score["cardiovascular"] = data.get("vasopressor_score", 0)
    score["cns"] = data.get("gcs_score", 0)
    score["renal"] = data.get("creatinine_score", 0)

    total = sum(score.values())

    return {
        "SOFA_components": score,
        "SOFA_total": total
    }


def apache_support():

    return {
        "system": "APACHE II",
        "purpose": "ICU severity assessment support"
    }
