# -*- coding: utf-8 -*-
# to be able use this ubuntu should have installed weather-api
#pip install weather-api
from Tkinter import *
from PIL import ImageTk, Image
import time, sys

class WEATHER:

    def __init__(self, master):

        self.master = master

        # Values
        self.vals = [StringVar() for i in range(6)]
        self.vals[0].set('Local current time: %s'%time.asctime(time.localtime(time.time())))
        self.vals[1].set('Temperature: F')
        self.vals[2].set('Barometer: in')
        self.vals[3].set('Humidity: %')
        self.vals[4].set('Sunrise')
        self.vals[5].set('Sunset')

        # Frames
        self.Conditions_Frame = LabelFrame(master, bg = 'white', text = 'Troy, NY, Weather for Today', font = ("Helvetica", 16), width = 600, height = 200)
        self.Conditions_Frame.pack_propagate(0)
        self.Conditions_Frame.pack(fill = None, expand = False, side = LEFT, anchor = NW, padx = 10, pady = 10)
        self.Cond_Values = Frame(self.Conditions_Frame, bg = 'white', bd = 0, padx = 10)
        self.Cond_Values.pack(fill = None, expand = False, side = LEFT, anchor = W)
        
        # Icon related        
        self.Cond_Icon = Frame(self.Conditions_Frame, bg = 'white', bd = 2)
        self.Cond_Icon.pack(side = TOP)
        self.ImgIcon = ImageTk.PhotoImage(Image.open('JPG/alien.jpg'))
        self.panel = Label(self.Cond_Icon, image = self.ImgIcon, borderwidth=0)
        self.panel.pack()

        # Labels
        self.labels = []
        for i in range(len(self.vals)):
            self.labels.append(Label(self.Cond_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.vals[i] ))
            self.labels[i].pack(anchor = W)

    def update(self, T, P, H, SS, SR, I):
        
        self.vals[0].set('Local current time: %s'% time.asctime(time.localtime(time.time())))
        self.vals[1].set('Temperature: %s %cF '  % (T, unichr(176)))
        self.vals[2].set('Barometer: %s mb'      % P)
        self.vals[3].set('Humidity: %s %%'       % H)
        self.vals[4].set('Sunrise: %s'           % SR)
        self.vals[5].set('Sunset: %s'            % SS)

        self.ImgIcon = ImageTk.PhotoImage(Image.open('JPG/'+I+'.jpg'))
        self.panel.config(image = self.ImgIcon)

        self.master.update()