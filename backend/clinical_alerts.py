# ClinRx-ICU-CCU Clinical Alerts Engine

def check_laboratory_alerts(labs):
    alerts = []

    if labs.get("potassium", 0) > 5.5:
        alerts.append({
            "type": "Critical",
            "issue": "Hyperkalemia",
            "action": "Review medications affecting potassium"
        })

    if labs.get("creatinine", 0) > 2:
        alerts.append({
            "type": "Warning",
            "issue": "Renal impairment",
            "action": "Consider renal dose adjustment"
        })

    return alerts


def check_vital_sign_alerts(vitals):
    alerts = []

    if vitals.get("MAP", 100) < 65:
        alerts.append({
            "type": "Critical",
            "issue": "Low MAP",
            "action": "Assess hemodynamic support"
        })

    if vitals.get("SpO2", 100) < 92:
        alerts.append({
            "type": "Warning",
            "issue": "Low oxygen saturation",
            "action": "Evaluate respiratory status"
        })

    return alerts
