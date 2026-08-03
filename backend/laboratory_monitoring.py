# ClinRx-ICU-CCU Laboratory Monitoring Module

def check_laboratory_values(labs):

    alerts = []

    if labs.get("potassium", 0) < 3.5:
        alerts.append({
            "parameter": "Potassium",
            "issue": "Hypokalemia",
            "action": "Consider potassium replacement and monitoring"
        })

    if labs.get("potassium", 0) > 5.0:
        alerts.append({
            "parameter": "Potassium",
            "issue": "Hyperkalemia",
            "action": "Review medications and ECG monitoring"
        })

    if labs.get("creatinine", 0) > 1.3:
        alerts.append({
            "parameter": "Creatinine",
            "issue": "Possible renal impairment",
            "action": "Review renal dose adjustment"
        })

    return alerts
