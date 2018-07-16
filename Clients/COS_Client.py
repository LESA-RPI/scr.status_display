from Client_util import *

if __name__ == "__main__":
    while True:
    	post_request('Status_COS', {"data": cos_control.read_all()})
        time.sleep(1)