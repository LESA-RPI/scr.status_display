'''
Author: Arunas Tuzikas, Martin Duffy
Description: Representing status information by using flask request
Date: 2/27/2017 updated 7/16/2018
'''

import time, json
from flask import Flask, jsonify, request, abort
from Status_Display import *

app = Flask(__name__)
display = Display()

@app.route('/Status_Weather', methods=['POST'])
def SetWeather():
    return updateModule('weather', ['temp', 'pressure', 'humidity', 'sunset', 'sunrise', 'icon'])

@app.route('/Status_Power', methods=['POST'])
def SetPower():
    return updateModule('power', ['current', 'voltage', 'activepower', 'apparentpower', 'powerfactor'])

@app.route('/Status_HVAC', methods=['POST'])
def SetHVAC():
    return updateModule('hvac', ['data'])

def updateModule(name, items):
    arguments = []
    for item in items:
        if not item in request.json:
            abort(400)
        arguments.append(request.json[item])
    display.frames[name].update(*arguments)
    return jsonify(request.json), 202

if __name__ == '__main__':
    display.root.update()
    app.run(host="192.168.0.61", port = 5000)