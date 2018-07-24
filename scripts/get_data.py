import sys, time, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../catkin_ws/src/scr_control/scripts/lights"))
import SCR_OctaLight_client as light_control
import multiprocessing

start = 0
stop = 10000
step = 190

def get_data(x):
	cct = 0
	lumens = 0
	x = float(x)
	cct = stop/2.0 - 0.00013 * (x - stop/2.0)**2
	lumens = 1900 - 0.00008 * (x - stop/2.0)**2
	return cct, lumens