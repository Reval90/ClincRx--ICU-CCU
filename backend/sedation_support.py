# ClinRx-ICU-CCU Sedation and Analgesia Support Engine

def sedation_review(patient):

    recommendations = []

    if patient.get("mechanical_ventilation"):
        recommendations.append({
            "issue": "Ventilated patient",
            "action": "Assess sedation requirement and target level"
        })

    if patient.get("sedation_score") == "deep":
        recommendations.append({
            "issue": "Deep sedation",
            "action": "Evaluate sedation reduction when appropriate"
        })

    if patient.get("pain_score", 0) > 6:
        recommendations.append({
            "issue": "Uncontrolled pain",
            "action": "Review analgesic therapy"
        })

    return recommendations
