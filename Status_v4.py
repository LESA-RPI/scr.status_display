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
    return updateModule('hvac', ['temp', 'humidity', 'ep', 'co2'])

@app.route('/Status_COS', methods=['POST'])
def SetCOS():
    return updateModule('cos', ['data'])

@app.route('/Status_TOF', methods=['POST'])
def SetTOF():
    return updateModule('tof', ['data'])

@app.route('/Status_TempChart', methods=['POST'])
def SetTempChart():
    return updateModule('tempchart', ['data'])

def updateModule(name, items):
    arguments = [request.json[item] for item in items]
    display.frames[name].update(*arguments)
    return jsonify(request.json), 202

if __name__ == '__main__':
    display.root.update()
    app.run(host="127.0.0.1", port = 5000)