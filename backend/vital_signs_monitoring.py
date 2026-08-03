# ClinRx-ICU-CCU Vital Signs Monitoring Module

def check_vital_signs(vitals):

    alerts = []

    if vitals.get("MAP", 100) < 65:
        alerts.append({
            "parameter": "MAP",
            "issue": "Low Mean Arterial Pressure",
            "action": "Assess hemodynamic support"
        })

    if vitals.get("SpO2", 100) < 92:
        alerts.append({
            "parameter": "SpO2",
            "issue": "Low oxygen saturation",
            "action": "Evaluate respiratory status"
        })

    if vitals.get("heart_rate", 0) > 120:
        alerts.append({
            "parameter": "Heart Rate",
            "issue": "Tachycardia",
            "action": "Assess clinical cause"
        })

    return alerts
