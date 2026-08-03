# ClinRx-ICU-CCU Therapeutic Drug Monitoring Engine

def check_drug_level(drug, level):

    recommendations = []

    if drug.lower() == "vancomycin":

        if level > 20:
            recommendations.append({
                "drug": "Vancomycin",
                "issue": "High drug concentration",
                "action": "Review dose and renal function"
            })

        elif level < 10:
            recommendations.append({
                "drug": "Vancomycin",
                "issue": "Low drug exposure",
                "action": "Evaluate dosing adequacy"
            })


    if drug.lower() in ["gentamicin", "amikacin"]:

        recommendations.append({
            "drug": drug,
            "action": "Monitor renal function and drug levels"
        })

    return recommendations
