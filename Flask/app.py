from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.save", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get input values from HTML form
    features = [
        float(request.form["u_q"]),
        float(request.form["coolant"]),
        float(request.form["u_d"]),
        float(request.form["motor_speed"]),
        float(request.form["i_d"]),
        float(request.form["i_q"]),
        float(request.form["pm"]),
        float(request.form["stator_yoke"]),
        float(request.form["ambient"]),
        float(request.form["torque"]),
        float(request.form["stator_tooth"])
    ]

    final_features = np.array([features])
    prediction = model.predict(final_features)

    return render_template(
        "index.html",
        prediction_text=f"Predicted Motor Temperature: {prediction[0]:.2f} °C"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000)

