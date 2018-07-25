from get_data import *

start = 0
stop = 10000
step = 25

def circ():
	
	for x in range(start, stop, step):
		x = float(x)
		cct, lumens = get_data(x)
		light_control.cct_all(int(cct),int(lumens))
		time.sleep(0.001)




if __name__ == "__main__":
	circ()