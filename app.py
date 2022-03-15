from turtle import color
from flask import Flask, request, jsonify, render_template
import pickle

#create flask app
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def home():
    if request.method == "POST":
        model = pickle.load(open('model.pkl', 'rb'))
        carat = request.form['']
        cut = request.form['']
        color = request.form['']
        clarity = request.form['']
        carat = request.form['']
        carat = request.form['']




        prediction = model.predict([[user_input]])
        print(prediction)
    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)