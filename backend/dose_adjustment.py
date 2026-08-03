# ClinRx-ICU-CCU Dose Adjustment Engine

def renal_dose_check(creatinine_clearance, medication):
    recommendations = []

    renal_adjusted_drugs = [
        "vancomycin",
        "piperacillin/tazobactam",
        "enoxaparin",
        "digoxin"
    ]

    if medication.lower() in renal_adjusted_drugs:

        if creatinine_clearance < 30:
            recommendations.append({
                "drug": medication,
                "alert": "Renal dose adjustment required",
                "reason": "Reduced renal clearance",
                "action": "Review dose and monitoring"
            })

    return recommendations
