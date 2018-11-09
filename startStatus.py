import libtmux

class Window():

	START_DIR = "~/scr.status_display"

	def __init__(self, name, command, start_dir = "~/catkin_ws"):
		self.name = name
		self.command = command
		self.start_dir = start_dir

	def create(self, session):
		print(self.name + " started")
		window = session.new_window(attach = False,
									window_name = self.name,
									start_directory = self.start_dir)

		pane = window.split_window(attach = False)
		pane.send_keys(self.command)

'''
------------------------------------
'''

SESSION_NAME = "Status"

WINDOWS = [Window("client_cos",     "python Clients/COS_Client.py"),
	       Window("client_hvac",    "python Clients/HVAC_Client.py"),
	       Window("client_tof",     "python Clients/TOF_Client.py"),
	       Window("client_power",   "python Clients/Power_Client.py"),
	       Window("client_weather", "python Clients/Weather_Client.py"),
	       Window("display", "python Status_v4.py"),
		  ]
'''
------------------------------------
'''

if __name__ == "__main__":
	server = libtmux.Server()

	try:
		session = server.find_where({"session_name": SESSION_NAME})
		session.kill_session()
		print("Session '" + SESSION_NAME + "' already exists, deleting...")
	except:
		pass

	session = server.new_session(attach = False,
								 session_name = SESSION_NAME,
								)

	for w in WINDOWS:
		w.create(session)

	print("Services started on tmux session '" + SESSION_NAME + "'")