import sys, time, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), "lights"))
import SCR_OctaLight_client as light_control
import multiprocessing
from get_data import *

start = 0
stop = 10000
step = 190

def cycle_light(x, y):
	for i in range(start, stop, step):
		i = float(i)
		cct, lumens = get_data(i)
		light_control.cct(x, y, int(cct),int(lumens))
		time.sleep(0.01)

def sun():
	row = 0
	lights = light_control.get_lights()
	lights.sort()

	cct, lumens, row = 0, 0, 0
	current_changing = []
	for light in lights:
		if(light[0] != row):
			current_changing = []
			row += 1
			time.sleep(0.2)
			
		current_changing.append(light)
			
		for l in current_changing:
			t = multiprocessing.Process(name = str(l), target = cycle_light, args = (l[0], l[1]))
			t.start()



if __name__ == "__main__":
	sun()



	
