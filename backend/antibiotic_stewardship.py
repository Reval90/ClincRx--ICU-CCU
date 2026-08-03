# ClinRx-ICU-CCU Antibiotic Stewardship Module

def antibiotic_review(therapy):

    recommendations = []

    if therapy.get("culture_available"):

        recommendations.append({
            "action": "Review culture results",
            "purpose": "Consider de-escalation"
        })

    if therapy.get("duration_days", 0) > 7:

        recommendations.append({
            "action": "Assess antibiotic duration",
            "purpose": "Avoid unnecessary prolonged therapy"
        })

    if therapy.get("renal_function") == "impaired":

        recommendations.append({
            "action": "Review renal dose adjustment",
            "purpose": "Prevent antibiotic toxicity"
        })

    return recommendations
