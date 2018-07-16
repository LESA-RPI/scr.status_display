# -*- coding: utf-8 -*-
from Tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import scipy
from scipy import ndimage 




class COS:
    def __init__(self, master):
        self.master = master
        
        self.Blind         = [[0 for x in range( 2)] for y in range( 2)]
        self.Blind_value   = [[0 for x in range( 2)] for y in range( 4)]

        ##TOF Frame
        self.COS_Frame = LabelFrame(master, bg = 'white', text = 'Color sensor readings', font = ("Helvetica", 16))
        self.COS_Frame.pack(side = LEFT, anchor = W, padx = 10, pady = 10)


    ##TOF self.plot_widget_TOF
        fig_COS = plt.figure(1, facecolor = 'white', figsize = (11.5, 4))
        self.canvas_COS = FigureCanvasTkAgg(fig_COS, master = self.COS_Frame)
        self.canvas_COS.get_tk_widget().configure(background = 'white', highlightcolor = 'white', highlightbackground = 'white')
        self.plot_widget_COS = self.canvas_COS.get_tk_widget()
        plt.draw()
        self.plot_widget_COS.grid(rowspan = 2,columnspan = 6, sticky=W)
        
        self.w1 = Canvas(self.COS_Frame, width=50, height=100, bg = 'white', bd=0, highlightthickness=0)
        self.w1.grid(row = 0 ,column = 0, sticky=S)
        self.w2 = Canvas(self.COS_Frame, width=50, height=100, bg = 'white', bd=0, highlightthickness=0)
        self.w2.grid(row = 1 ,column = 0, sticky=N)
        self.wa = Canvas(self.COS_Frame, width=100, height=50, bg = 'White', bd=0, highlightthickness=0)
        self.wa.grid(row = 3 ,column = 1, sticky=W+S)
        self.wb = Canvas(self.COS_Frame, width=100, height=50, bg = 'white', bd=0, highlightthickness=0)
        self.wb.grid(row = 3 ,column = 2, sticky=W+S)
        self.wc = Canvas(self.COS_Frame, width=100, height=50, bg = 'white', bd=0, highlightthickness=0)
        self.wc.grid(row = 3 ,column = 3, sticky=W+S)
        
        
        
        
        self.w3 = Canvas(self.COS_Frame, width=100, height=50, bg = 'white', bd=0, highlightthickness=0)
        self.w3.grid(row = 3 ,column = 4, sticky=E+N)
        self.w4 = Canvas(self.COS_Frame, width=100, height=50, bg = 'white', bd=0, highlightthickness=0)
        self.w4.grid(row = 3 ,column = 5, sticky=W+N)

        
        ## self.Blinders related
        self.Blind[0][0] = self.w3.create_rectangle( 2, 0, 98, 25, width = 2)
        self.Blind[0][1] = self.w4.create_rectangle( 2, 0, 98, 25, width = 2)
        self.Blind[1][0] = self.w1.create_rectangle(25, 2, 50, 98, width = 2)
        self.Blind[1][1] = self.w2.create_rectangle(25, 2, 50, 98, width = 2)
        self.Blind_value[0][0] = self.w3.create_text(50, 40, font="Times 12", text ="100%; 90o")
        self.Blind_value[1][0] = self.w4.create_text(50, 40, font="Times 12", text ="100%; 90o")
        self.Blind_value[2][0] = self.w1.create_text(10, 50, font="Times 12", text ="100%; 90o", angle=90)
        self.Blind_value[3][0] = self.w2.create_text(10, 50, font="Times 12", text ="100%; 45o", angle=90)
        
    
    def SetVal_E(self, la, lb, ta, tb):
        #self.Blind_Ea = np.exp((lb-100)/100)*0.02*ta
        #self.Blind_Eb = ((100+lb*0.3)+tb*2)/2
        #print la, ta, self.Blind_Ea
        #print('#%02x%02x%02x'%(int(255*self.Blind_Ea), int(255*self.Blind_Ea), int(255*self.Blind_Ea)))
        
        self.w1.itemconfig(self.Blind[1][0], fill = '#%02x%02x%02x'%(int(2.55*la), int(2.55*ta*2), int(2.55*ta*2)))
        self.w2.itemconfig(self.Blind[1][1], fill = '#%02x%02x%02x'%(int(2.55*lb), int(2.55*tb*2), int(2.55*tb*2)))
        self.w1.itemconfig(self.Blind_value[2][0], text ="%d%%; %d%c"%(la, int(ta*1.8), unichr(176)))
        self.w2.itemconfig(self.Blind_value[3][0], text ="%d%%; %d%c"%(lb, int(tb*1.8), unichr(176)))
        
    def SetVal_N(self, la, lb, ta, tb):

        #self.Blind_Na = np.exp((lb-100)/100)*0.02*ta
        #self.Blind_Nb = ((100+lb*0.3)+tb*2)/2
        
        #print la, ta, self.Blind_Na
        
        #self.w3.itemconfig(self.Blind[0][0], fill = '#%02x%02x%02x'%(int(2.55*self.Blind_Na), int(2.55*self.Blind_Na), int(2.55*self.Blind_Na)))
        #self.w4.itemconfig(self.Blind[0][1], fill = '#%02x%02x%02x'%(int(2.55*self.Blind_Nb), int(2.55*self.Blind_Nb), int(2.55*self.Blind_Nb)))
        self.w3.itemconfig(self.Blind[0][0], fill = '#%02x%02x%02x'%(int(2.55*la), int(2.55*ta*2), int(2.55*ta*2)))
        self.w4.itemconfig(self.Blind[0][1], fill = '#%02x%02x%02x'%(int(2.55*lb), int(2.55*tb*2), int(2.55*tb*2)))
          
        self.w3.itemconfig(self.Blind_value[0][0], text ="%d%%; %d%c"%(la, int(ta*1.8), unichr(176)))
        self.w4.itemconfig(self.Blind_value[1][0], text ="%d%%; %d%c"%(lb, int(tb*1.8), unichr(176)))
        
        
        
        
	

    def Plot_COS(self, B):
        B = np.asarray(B)
        B = B.reshape(5, 14, 3)
        #A = B
        plt.cla()
        plt.clf()
        B=B[::-1]
        B = B[:,::-1]

        for x in range (0, 14):
            for k in range (0, 5):
                for l in range (0, 3):
                    A[k][x][l] = B[4-k][13-x][l]
        plt.imshow(B, interpolation = 'none')
        self.canvas_COS.draw()
