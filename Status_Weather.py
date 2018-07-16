# -*- coding: utf-8 -*-
# to be able use this ubuntu should have installed weather-api
#pip install weather-api
from Tkinter import *
from pyowm import OWM
from datetime import datetime
from dateutil import tz
from PIL import ImageTk, Image
from pytz import timezone, utc

import time
import sys

class WEATHER:
    def __init__(self, master):
        self.master = master
        
        self.val_C  = StringVar() #todays date
        self.val_T  = StringVar() #Temperature
        self.val_P  = StringVar() #Preasure
        self.val_H  = StringVar() #Humidity
        self.val_SR = StringVar() #Sunrise
        self.val_SS = StringVar() #Sunset

        #self.Conditions (Temperature, Humadity and so on) Values
        self.Conditions_Frame = LabelFrame(master, bg = 'white', text = 'Troy, NY, Weather for Today', font = ("Helvetica", 16), width = 600, height = 200)
        self.Conditions_Frame.pack_propagate(0)
        self.Conditions_Frame.pack(fill = None, expand = False, side = LEFT, anchor = NW, padx = 10, pady = 10)
        
        self.Cond_Values = Frame(self.Conditions_Frame, bg = 'white', bd = 0, padx = 10)
        self.Cond_Values.pack(fill = None, expand = False, side = LEFT, anchor = W)
        
        #Icon related        
        self.Cond_Icon = Frame(self.Conditions_Frame, bg = 'white', bd = 2)
        self.Cond_Icon.pack(side = TOP)
        self.ImgIcon = ImageTk.PhotoImage(Image.open('JPG/alien.jpg'))
        self.panel = Label(self.Cond_Icon, image = self.ImgIcon, borderwidth=0)
        self.panel.pack()
        
        self.val_C.set('Local current time: %s'%time.asctime(time.localtime(time.time())))
        self.val_T.set('Temperature: F')
        self.val_P.set('Barometer: in')
        self.val_H.set('Humidity: %')
        self.val_SR.set('Sunrise')
        self.val_SS.set('Sunset')
       
        self.Label_C  = Label(self.Cond_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_C )
        self.Label_T  = Label(self.Cond_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_T )
        self.Label_P  = Label(self.Cond_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_P )
        self.Label_H  = Label(self.Cond_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_H )
        self.Label_SR = Label(self.Cond_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_SR)
        self.Label_SS = Label(self.Cond_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_SS)
       
        self.Label_C.pack(anchor = W)
        self.Label_T.pack(anchor = W)
        self.Label_P.pack(anchor = W)
        self.Label_H.pack(anchor = W)
        self.Label_SR.pack(anchor = W)
        self.Label_SS.pack(anchor = W)
       
        
    def update(self, T, P, H, SS, SR, I):

        self.val_C.set('Local current time: %s'%time.asctime(time.localtime(time.time())))
        self.val_T.set('Temperature: %s %cF '%(T, unichr(176)))
        self.val_P.set('Barometer: %s mb'%P)
        self.val_H.set('Humidity: %s %%'%H)
        self.val_SR.set('Sunrise: %s'%SR)
        self.val_SS.set('Sunset: %s'%SS)
            
        self.master.update()