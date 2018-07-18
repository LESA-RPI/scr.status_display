from Client_util import *

if __name__ == "__main__":
    while True:
    	post_request('Status_TOF', {"data": tof_control.get_distances()})
        time.sleep(.3)