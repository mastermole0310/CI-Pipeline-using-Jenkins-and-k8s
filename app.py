import os
from flask import Flask, render_template, abort, url_for, json, jsonify, Response
import json

app = Flask(__name__,template_folder='.')

with open('my_json.json', 'r') as myfile:
    data = myfile.read()

@app.route("/version")
def index():
    return  Response(data, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
