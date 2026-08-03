# ClinRx-ICU-CCU Sepsis Clinical Support Engine

def sepsis_assessment(patient_data):

    recommendations = []

    if patient_data.get("lactate", 0) >= 2:
        recommendations.append({
            "issue": "Elevated lactate",
            "action": "Assess perfusion and sepsis severity"
        })

    if patient_data.get("MAP", 100) < 65:
        recommendations.append({
            "issue": "Low MAP",
            "action": "Evaluate fluid status and vasopressor support"
        })

    if patient_data.get("suspected_infection"):

        recommendations.append({
            "issue": "Possible infection",
            "action": "Review cultures and antimicrobial therapy"
        })

    return recommendations
