import time, sys, requests
sys.path.append("../../catkin_ws/src/scr_control/scripts/HVAC")
sys.path.append("../../catkin_ws/src/scr_control/scripts/time_of_flight")
sys.path.append("../../catkin_ws/src/scr_control/scripts/color_sensors")
sys.path.append("../../catkin_ws/src/scr_control/scripts/lights")
import SCR_HVAC_client as hvac_control
import SCR_TOF_client  as tof_control
import SCR_COS_client  as cos_control
import SCR_OctaLight_client  as light_control
import numpy as np

def post_request(name, data):
	requests.post('http://192.168.0.2:5000/'+name, json=data)