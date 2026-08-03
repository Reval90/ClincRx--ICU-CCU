from flask import Flask, jsonify, render_template

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Main Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Patient Profile
@app.route("/patient")
def patient_profile():
    return render_template("patient_profile.html")


# Medication Review
@app.route("/medications/review")
def medication_review():
    return render_template("medication_review.html")


# Patient API
@app.route("/patients")
def patients():
    return jsonify({
        "patients": [],
        "message": "Patient module initialized"
    })


# Medication API
@app.route("/medications")
def medications():
    return jsonify({
        "medications": [],
        "message": "Medication module initialized"
    })


# Clinical Alerts API
@app.route("/alerts")
def alerts():
    return jsonify({
        "alerts": [],
        "message": "Clinical alerts module initialized"
    })


# System Status
@app.route("/status")
def status():
    return jsonify({
        "system": "ClinRx-ICU-CCU",
        "status": "Running"
    })


if __name__ == "__main__":
    app.run(debug=True)
