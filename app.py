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


if __name__ == "__main__":
    app.run(debug=True)
