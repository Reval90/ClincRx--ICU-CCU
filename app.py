from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "system": "ClinRx-ICU-CCU",
        "status": "Clinical Decision Support System Running"
    })

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

if __name__ == "__main__":
    app.run(debug=True)
