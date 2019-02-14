import requests

def post_request(name, data):
	requests.post('http://192.168.0.2:5000/' + name, json=data)

post_request('Status_Occupancy', {"Total": 8,
				  "Standing": 2,
				  "Sitting": 4,
				  "Lying": 0})
