from get_data import *

start = 0
stop = 10000
step = 100

# def cycle_light(x, y):
# 	for i in range(start, stop, step):
# 		i = float(i)
# 		cct, lumens = get_data(i)
# 		light_control.cct(x, y, int(cct),int(lumens))

# def sun():
# 	row = 0
# 	lights = light_control.get_lights()
# 	lights.sort()

# 	cct, lumens, row = 0, 0, 0
# 	current_changing = []
# 	for light in lights:
# 		if(light[0] != row):
# 			current_changing = []
# 			row += 1
# 			time.sleep(0.2)
			
# 		current_changing.append(light)
			
# 		for l in current_changing:
# 			t = multiprocessing.Process(name = str(l), target = cycle_light, args = (l[0], l[1]))
# 			t.start()


def sun():
	lights = light_control.get_lights()
	lights.sort()

	space = 200

	for i in range(start, stop + space * 7, step):
		i = float(i)

		cct, lumens = get_data(i)
		light_control.cct(lights[0][0], lights[0][1], int(cct),int(lumens))
		light_control.cct(lights[1][0], lights[1][1], int(cct),int(lumens))

		cct, lumens = get_data(i - space)
		light_control.cct(lights[2][0], lights[2][1], int(cct),int(lumens))

		cct, lumens = get_data(i - 2 * space)
		light_control.cct(lights[3][0], lights[3][1], int(cct),int(lumens))
		light_control.cct(lights[4][0], lights[4][1], int(cct),int(lumens))

		cct, lumens = get_data(i - 4 * space)
		light_control.cct(lights[5][0], lights[5][1], int(cct),int(lumens))
		light_control.cct(lights[6][0], lights[6][1], int(cct),int(lumens))

		cct, lumens = get_data(i - 5 * space)
		light_control.cct(lights[7][0], lights[7][1], int(cct),int(lumens))

		cct, lumens = get_data(i - 6 * space)
		light_control.cct(lights[8][0], lights[8][1], int(cct),int(lumens))
		light_control.cct(lights[9][0], lights[9][1], int(cct),int(lumens))



if __name__ == "__main__":
	sun()



	
