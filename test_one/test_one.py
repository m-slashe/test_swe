from flask import Flask
from flask import request
from statistics import mean, median
from numpy import percentile

app = Flask(__name__)


@app.route("/min")
def get_min():
    list_numbers = request.args.getlist('numbers', type=int) or []
    quantifier = request.args.get('quantifier', type=int) or 0
    max_numbers = []
    for _ in range(quantifier):
        max_value = min(list_numbers)
        max_numbers.append(max_value)
        list_numbers.remove(max_value)
    return {'data': max_numbers}


@app.route("/max")
def get_max():
    list_numbers = request.args.getlist('numbers', type=int) or []
    quantifier = request.args.get('quantifier', type=int) or 0
    max_numbers = []
    for _ in range(quantifier):
        max_value = max(list_numbers)
        max_numbers.append(max_value)
        list_numbers.remove(max_value)
    return {'data': max_numbers}


@app.route("/avg")
def get_avg():
    list_numbers = request.args.getlist('numbers', type=int) or []
    return {'data': mean(list_numbers)}


@app.route("/median")
def get_median():
    list_numbers = request.args.getlist('numbers', type=int) or []
    return {'data': median(list_numbers)}


@app.route("/percentile")
def get_percentile():
    list_numbers = request.args.getlist('numbers', type=int) or []
    quantifier = request.args.get('quantifier', type=int) or 0
    # TODO: Verify if it should be implemented by hand
    return {'data': percentile(list_numbers, quantifier)}
