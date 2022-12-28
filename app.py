from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import pickle
app = Flask(__name__)


# prediction function
def ValuePredictor(to_predict_list):
	to_predict = np.array(to_predict_list).reshape(1, 8)
	loaded_model = pickle.load(open("best_model.pickle", "rb"))
	result = loaded_model.predict(to_predict)
	return result[0]



@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result', methods = ['POST'])
def result():
    # print(request)
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        prediction = ValuePredictor(to_predict_list)
        prediction *= 100000
        return render_template("index.html", prediction = prediction)

        


# @app.route('/result', methods = ['POST'])
# def result():
# 	if request.method == 'POST':
		