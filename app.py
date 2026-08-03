from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/icu")
def icu_overview():
    return render_template("icu_overview.html")


@app.route("/patient")
def patient_profile():
    return render_template("patient_profile.html")


@app.route("/medications/review")
def medication_review():
    return render_template("medication_review.html")


@app.route("/interactions")
def drug_interaction():
    return render_template("drug_interaction.html")


@app.route("/alerts")
def clinical_alerts():
    return render_template("clinical_alerts.html")


@app.route("/laboratory")
def laboratory_monitoring():
    return render_template("laboratory_monitoring.html")


@app.route("/vitals")
def vital_signs():
    return render_template("vital_signs.html")


@app.route("/tdm")
def tdm_dashboard():
    return render_template("tdm_dashboard.html")


@app.route("/sepsis")
def sepsis_dashboard():
    return render_template("sepsis_dashboard.html")


@app.route("/anticoagulation")
def anticoagulation_dashboard():
    return render_template("anticoagulation_dashboard.html")


@app.route("/nutrition")
def nutrition_dashboard():
    return render_template("nutrition_dashboard.html")


@app.route("/status")
def status():
    return jsonify({
        "system": "ClinRx-ICU-CCU",
        "status": "Running",
        "modules": "Active"
    })


if __name__ == "__main__":
    app.run(debug=True)
