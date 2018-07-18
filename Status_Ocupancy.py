# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import ImageTk, Image

class OCCUPANCY:
    def __init__(self, master):
        self.master = master

        self.val_Sit = StringVar()
        self.val_Sta = StringVar()
        self.val_Tot = StringVar()
        self.val_Lyi = StringVar()
        self.pro_sta = StringVar()

        self.val_Sit.set('Number of standing people:')
        self.val_Sta.set('Number of sitting people:')
        self.val_Tot.set('Total number of people:')
        self.val_Lyi.set('Number of lying people:')        
        self.pro_sta.set('Projector is:')
        
        self.Occupancy_Frame = LabelFrame(master, bg = 'white', text = 'Room Status', font = ("Helvetica", 16), width = 600, heigh = 200)
        self.Occupancy_Frame.pack_propagate(0)
        self.Occupancy_Frame.pack(fill = None, expand = False, side = LEFT, anchor = NW, padx = 10, pady = 10)

        self.Occupancy_Values = Frame(self.Occupancy_Frame, bg = 'white', bd = 0, padx = 10)
        self.Occupancy_Values.pack(fill = None, expand = False, side = LEFT, anchor = W)
        
        self.Label_Tota  = Label(self.Occupancy_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_Tot )
        self.Label_Sitt  = Label(self.Occupancy_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_Sit )
        self.Label_Stan  = Label(self.Occupancy_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_Sta )
        self.Label_Lyin  = Label(self.Occupancy_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_Lyi )
        
        self.Label_Proj  = Label(self.Occupancy_Values, bg = 'white', font = ("Helvetica", 14), textvariable = self.pro_sta )
        
        self.Label_Tota.pack(anchor = W)
        self.Label_Sitt.pack(anchor = W)
        self.Label_Stan.pack(anchor = W)
        #self.Label_Lyin.pack(anchor = W)
        self.Label_Proj.pack(anchor = W)

    	#Icon related        
    	self.Ocup_Icon = Frame(self.Occupancy_Frame, bg = 'white', bd = 2)
    	self.Ocup_Icon.pack(side = TOP)
    	self.ImgIcon = ImageTk.PhotoImage(Image.open('JPG/meeting.jpg'))
    	self.panel = Label(self.Ocup_Icon, image = self.ImgIcon, borderwidth=0)
    	self.panel.pack()
    	
    def SetOcu(self, Total, Sitting, Standing, Lying): 
        self.val_Tot.set('Total number of people: %d'   %Total)
        self.val_Sit.set('Number of standing people: %d'%Standing)
        self.val_Sta.set('Number of sitting people: %d' %Sitting)
        self.val_Lyi.set('Number of lying people: %d'   %Lying)
        if Lying > 0: 
            self.ImgIcon = ImageTk.PhotoImage(Image.open('JPG/emergency.jpg'))
            self.panel.config(image = self.ImgIcon)
        return 0
        
    def SetPro(self, Status):
        self.pro_sta.set('Projector is: %s'%Status)
        if Status == 'ON': 
            self.ImgIcon = ImageTk.PhotoImage(Image.open('JPG/projector.jpg'))
            self.panel.config(image = self.ImgIcon)
        else:
            self.ImgIcon = ImageTk.PhotoImage(Image.open('JPG/meeting.jpg'))
            self.panel.config(image = self.ImgIcon)
        return 0      