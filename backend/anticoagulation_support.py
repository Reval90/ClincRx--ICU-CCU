# ClinRx-ICU-CCU Anticoagulation Support Engine

def anticoagulation_review(patient):

    recommendations = []

    if patient.get("bleeding_risk") == "high":
        recommendations.append({
            "issue": "High bleeding risk",
            "action": "Review anticoagulant therapy"
        })

    if patient.get("renal_function") == "impaired":
        recommendations.append({
            "issue": "Renal impairment",
            "action": "Evaluate anticoagulant dose adjustment"
        })

    if patient.get("anticoagulant") in ["warfarin", "heparin"]:
        recommendations.append({
            "issue": "Monitoring required",
            "action": "Review INR/aPTT and clinical status"
        })

    return recommendations
