import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#create flask app
app = Flask(__diamond-predictor__)

#load the pickle model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    return render_template("index.html", prediction_text = "The price of the diamond is {}".format(prediction))

if __diamond-predictor__ = "__main__":
    app.run(debug=True)