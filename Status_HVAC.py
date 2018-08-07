# -*- coding: utf-8 -*-
from Tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class HVAC:
	def __init__(self, master):
		self.master = master

		# Member variables and HVAC objects
		self.CeilingPlates = [[0 for x in range( 5)] for y in range(14)]
		self.Lights		   = [ 0 for x in range(10)]
		self.Heaters	   = [[0 for x in range( 2)] for y in range( 2)]
		self.Heater_value  = [ 0 for x in range( 2)]
		self.HVAC_HE	   = [ 0 for x in range (2)]
		self.HVAC_AC	   = [ 0 for x in range (2)]
		self.HVAC_value	   = [ 0 for x in range (2)]
		self.HVAC_sens	   = [ 0 for x in range (7)]
		self.HVAC_sens_val = [ 0 for x in range (7)]
		self.Lights_val	   = [ 0 for x in range(10)]
		self.Light_C	   = [[0 for x in range( 5)] for y in range(10)]
		
		# Main frame and cavas
		self.HVAC_Frame = LabelFrame(master, bg = 'white', text = 'HVAC control', font = ("Helvetica", 16))
		self.HVAC_Frame.pack(side = LEFT, anchor = W, padx = 10, pady = 10)
		self.w = Canvas(self.HVAC_Frame, width=800, height=250, bg='white', bd=0, highlightthickness=0)
		self.w.pack()

		# Sensor values
		sens_coords = [(50, 0), (300, 220), (475, 220), (700, 0), (300, 0), (450, 0), (500, 0)]
		default_sens_values = ["XX.XC"] * 5  + ["XX%", "XXp"]
		for i in range(7):
			x, y = sens_coords[i]
			self.HVAC_sens[i] = self.w.create_oval(x,  y, x + 50, y + 20, fill = 'white')
			self.HVAC_sens_val[i] = self.w.create_text(x + 25, y + 10, font="times 10", text = default_sens_values[i])
		
		# Heaters related
		self.Heaters[0][0] = self.w.create_rectangle(700, 225, 800, 250)
		self.Heaters[0][1] = self.w.create_rectangle(600, 225, 700, 250)
		self.Heaters[1][0] = self.w.create_rectangle(0,  25, 25, 125)
		self.Heaters[1][1] = self.w.create_rectangle(0, 125, 25, 225)
	
		self.Heater_value[0] = self.w.create_text(700, 240, font="Times 15 bold", text="XX%")
		self.Heater_value[1] = self.w.create_text(10,  125, font="Times 15 bold", text="XX%", angle=90)
		
		# Init ceiling plates
		for i in range (0, 14):
	  		for k in range (0, 5):
				self.CeilingPlates[i][k] = self.w.create_rectangle(50+50*i, 20+40*k, 50*i+100, 40*k+60) 
	   
		# self.Lights wit ceiling plates binding
		self.Lights[0] = self.CeilingPlates[ 1][1]
		self.Lights[1] = self.CeilingPlates[ 1][3]
		self.Lights[2] = self.CeilingPlates[ 3][2]
		self.Lights[3] = self.CeilingPlates[ 5][1]
		self.Lights[4] = self.CeilingPlates[ 5][3]
		self.Lights[5] = self.CeilingPlates[ 8][1]
		self.Lights[6] = self.CeilingPlates[ 8][3]
		self.Lights[7] = self.CeilingPlates[10][2]
		self.Lights[8] = self.CeilingPlates[12][1]
		self.Lights[9] = self.CeilingPlates[12][3]

		# Init self.Lights	   
		for i in range (0, 10):
			self.w.itemconfig(self.Lights[i], fill = 'yellow')

		# Init HVAC air
		self.HVAC_HE[0] = self.w.create_rectangle(250, 100, 350, 140)
		self.HVAC_HE[1] = self.w.create_rectangle(350, 100, 400, 140)
		self.HVAC_AC[0] = self.w.create_rectangle(400, 100, 450, 140)
		self.HVAC_AC[1] = self.w.create_rectangle(450, 100, 550, 140)
		self.w.itemconfig(self.HVAC_HE[0], fill = 'red')
		self.w.itemconfig(self.HVAC_HE[1], fill = 'orange red')
		self.w.itemconfig(self.HVAC_AC[0], fill = 'blue')
		self.w.itemconfig(self.HVAC_AC[1], fill = 'deep sky blue')
		self.HVAC_value[0] = self.w.create_text(325, 120, font="Times 15 bold", text="XX%")
		self.HVAC_value[1] = self.w.create_text(475, 120, font="Times 15 bold", text="XX%")
		
	def update(self, temp, humidity, ep, co2):
		# Init self.Lights	   
		new_vals = [temp[0], temp[1], temp[2], temp[3], temp[4], humidity, co2]
		for i in range(7):
			self.w.itemconfigure(self.HVAC_sens_val[i], text = new_vals[i])
		for i in range(2):
			self.w.itemconfigure(self.Heater_value[i], text = ep[i])
			self.w.itemconfigure(self.HVAC_value[i],   text = ep[i+2])

		self.master.update()
