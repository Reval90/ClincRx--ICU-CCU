# ClinRx-ICU-CCU Pharmacist Intervention Module

interventions = []


def add_intervention(intervention_data):
    interventions.append(intervention_data)

    return {
        "status": "success",
        "message": "Clinical intervention recorded"
    }


def get_interventions():
    return interventions


def update_intervention_status(index, status):

    if index < len(interventions):
        interventions[index]["status"] = status

        return {
            "status": "success",
            "message": "Intervention status updated"
        }

    return {
        "status": "error",
        "message": "Intervention not found"
      }
