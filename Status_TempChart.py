from Tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import scipy
import time
from scipy import ndimage 
from scipy.ndimage.interpolation import shift

class TempChart:
    def __init__(self, master):
        self.master = master
        
        self.Temp     = [0 for x in range(98)]
        self.CO2      = [0 for x in range(98)]
        self.GlobalTime = time.time()
        
        self.TempChart_Frame = LabelFrame(master, bg = 'white', text = '24 hours temperature and CO2 readings', font = ("Helvetica", 16))
        self.TempChart_Frame.pack(side = LEFT, anchor = W, padx = 10, pady = 10)
        
        self.w = Canvas(self.TempChart_Frame, width=1050, height=250, bg='white', bd=0, highlightthickness=0)
        self.w.pack()

        # coordinats axis

        self.w.create_line(  50, 220, 1000, 220, width = 2)
        
        self.w.create_line(  50,  30,   50, 220, width = 2)
        self.w.create_line(  50,  30,   45, 45, width = 2)
        self.w.create_line(  50,  30,   55, 45, width = 2)
        
        self.w.create_line(1000,  30, 1000, 220, width = 2)
        self.w.create_line(1000,  30,  995, 45, width = 2)
        self.w.create_line(1000,  30, 1005, 45, width = 2)
    
        self.w.create_text(10, 125, font="times 12", text = 'Temperature (%cC)'%unichr(176), fill = 'red', angle=90)
        self.w.create_text(1035, 125, font="times 12", text = 'CO2 (ppm)', fill = 'green', angle=90)

        
        # create little lines accros x
        for x in range(1, 26):
            self.w.create_line(50+38*x, 210, 50+38*x, 220, width = 2)    
            self.w.create_line(50+38*x, 220, 50+38*x,  30, width = 1, dash=(4,4))   
            self.w.create_text(50+38*(x-1), 235, font="times 10", text = str(x-25))

            
        for x in range(1, 7):
            self.w.create_line(  50, 220-31*x,  60, 220-31*x, width = 2)    
            self.w.create_line(1000, 220-31*x, 990, 220-31*x, width = 2)    
            self.w.create_line(  50, 220-31*x, 1000, 220-31*x, width = 1, dash=(4,4))   

        for x in range(1, 6):
            self.w.create_text(  35, 220-31*x, font="times 10", text = str(18+x), fill = 'red')
            self.w.create_text(1015, 220-31*x, font="times 10", text = str(400+x*100), fill = 'green')
            
            yy = 220
            xx = 9.5 #19 
            ii = 220
        for x in range(0, 97):
            self.Temp[x] = self.w.create_oval( 50+(xx*x)-4, yy-4, 50+(xx*x)+4, yy+4, fill = 'red', width = 0)
            self.CO2[x] = self.w.create_oval( 50+(xx*x)-4, ii-4, 50+(xx*x)+4, ii+4, fill = 'green', width = 0)
        
    def update(self, T, CO):

        print(T, CO)

        if (time.time() - self.GlobalTime) > 900: #900 
            self.GlobalTime = time.time()
            print self.GlobalTime
            for x in range(0, 97):
                a = self.w.coords(self.Temp[x  ])[0]
                b = self.w.coords(self.Temp[x+1])[1]
                c = self.w.coords(self.Temp[x  ])[2]
                d = self.w.coords(self.Temp[x+1])[3]
                self.w.coords(self.Temp[x], a, b, c, d)
                g = self.w.coords(self.CO2[x  ])[0]
                h = self.w.coords(self.CO2[x+1])[1]
                i = self.w.coords(self.CO2[x  ])[2]
                j = self.w.coords(self.CO2[x+1])[3]
                self.w.coords(self.CO2[x], g, h, i, j)
                
       
        Y_coord=-31.104*T+779.8765           
        self.w.coords(self.Temp[96], 50+(9.5*96)-4, Y_coord-4, 50+(9.5*96)+4, Y_coord+4)
        
        Y_coord=-0.31*CO+344           
        self.w.coords(self.CO2[96], 50+(9.5*96)-4, Y_coord-4, 50+(9.5*96)+4, Y_coord+4)
