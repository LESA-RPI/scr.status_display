import time, threading
from Tkinter import *
from PIL import ImageTk, Image

from Status_Power import POWER
from Status_Weather import WEATHER
from Status_Ocupancy import OCCUPANCY
from Status_TOF import TOF
from Status_COS import COS
from Status_HVAC import HVAC
from Status_TempChart import TempChart

class Display():

	def __init__(self):

		# Implementation of GUI
		self.root = Tk()
		self.root.attributes('-fullscreen', True)
		self.root.configure(background = "White")

		# Sections
		self.sections = {}
		self.frames = {}

		# LESA banner
		self.sections["banner"] = Frame(self.root, bg = 'white')
		self.sections["banner"].pack(side = TOP)
		self.LESA_b = ImageTk.PhotoImage(Image.open("Pic/LESA.png"))
		self.Banner = Label(self.sections["banner"], image = self.LESA_b, borderwidth=0)
		self.Banner.pack()

		# Second Frame
		self.sections["top"] = Frame(self.root, bg = 'white')
		self.sections["top"].pack(side = TOP)

		# Second Frame
		self.sections["middle"] = Frame(self.root, bg = 'white')
		self.sections["middle"].pack(side = TOP)

		# Third Frame
		self.sections["bottom"] = Frame(self.root, bg = 'white')
		self.sections["bottom"].pack(side = TOP)

		self.frames["power"] = POWER(self.sections['top'])

		self.frames["weather"] = WEATHER(self.sections['top'])

		self.frames["occupancy"] = OCCUPANCY(self.sections['top'])

		self.frames["tof"] = TOF(self.sections['middle'])
		self.frames["cos"] = COS(self.sections['middle'])

		self.frames["hvac"] = HVAC(self.sections['bottom'])
		self.frames["tempchart"] = TempChart(self.sections['bottom'])

		# Other member variables
		self.loop = 0