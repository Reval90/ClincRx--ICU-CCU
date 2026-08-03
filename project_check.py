# ClinRx-ICU-CCU Project Structure Checker

import os


required_files = [
    "app.py",
    "requirements.txt",
    "templates/index.html",
    "templates/dashboard.html",
    "templates/patient_profile.html",
    "templates/medication_review.html",
    "templates/clinical_alerts.html",
    "templates/laboratory_monitoring.html",
    "templates/vital_signs.html",
    "templates/tdm_dashboard.html",
    "templates/sepsis_dashboard.html",
    "templates/anticoagulation_dashboard.html",
    "templates/nutrition_dashboard.html"
]


def check_project():

    missing = []

    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print("Missing files:")
        for item in missing:
            print(item)

    else:
        print("ClinRx-ICU-CCU structure is complete")


if __name__ == "__main__":
    check_project()
