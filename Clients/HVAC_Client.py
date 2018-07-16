from Client_util import *

if __name__ == "__main__":
    while True:
    	lights = []
    	for light in light_control.get_lights():
    		print(light)
    		sources = light_control.get_sources(light[0], light[1])
    		print(sources)
    		on = False
    		for c in sources:
    			if c > 0:
    				on = True
    		lights.append(on)

    	post_request('Status_HVAC', {"data": lights})
        time.sleep(5)