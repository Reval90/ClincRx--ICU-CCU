# ClinRx-ICU-CCU Drug Interaction Engine

def check_interactions(medications):
    alerts = []

    if "warfarin" in medications and "aspirin" in medications:
        alerts.append({
            "severity": "Major",
            "interaction": "Warfarin + Aspirin",
            "risk": "Increased bleeding risk",
            "action": "Monitor bleeding and reassess therapy"
        })

    if "rivaroxaban" in medications and "clarithromycin" in medications:
        alerts.append({
            "severity": "Major",
            "interaction": "Rivaroxaban + Clarithromycin",
            "risk": "Increased anticoagulant effect",
            "action": "Evaluate bleeding risk"
        })

    return alerts
