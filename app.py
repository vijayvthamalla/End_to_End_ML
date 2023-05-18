import pickle
from flask import Flask, request, jsonify, app, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('regmodel.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_data)
    return jsonify(output[0])

@app.route('/predict/',methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    print(data)
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    final_output = model.predict(final_input)
    print(final_output)
    return render_template("predict.html",prediction=f"Predicted price of House based on given input is {final_output[0]:.2f}")

if __name__=="__main__":
    app.run(debug=True)

