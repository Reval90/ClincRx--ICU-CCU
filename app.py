from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/patients")
def patients():
    return jsonify({
        "patients": [],
        "message": "Patient module initialized"
    })


@app.route("/medications")
def medications():
    return jsonify({
        "medications": [],
        "message": "Medication module initialized"
    })


@app.route("/alerts")
def alerts():
    return jsonify({
        "alerts": [],
        "message": "Clinical alerts module initialized"
    })
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/patient")
def patient_profile():
    return render_template("patient_profile.html")

if __name__ == "__main__":
    app.run(debug=True)
