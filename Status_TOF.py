# -*- coding: utf-8 -*-
from Tkinter import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class TOF:
    def __init__(self, master):

        self.master = master
        
        # TOF Frame
        self.TOF_Frame = LabelFrame(master, bg = 'white', text = 'Time-of-flight sensor readings', font = ("Helvetica", 16))
        self.TOF_Frame.pack(side = LEFT, anchor = W, padx = 10, pady = 10)
        self.w = Canvas(self.TOF_Frame, width=100, height=50, bg = 'white', bd=0, highlightthickness=0)
        self.w.pack(side = BOTTOM)

        # plot_widget
        self.fig_TOF = plt.figure(1, facecolor = 'white', figsize = (11.5, 4))
        self.canvas_TOF = FigureCanvasTkAgg(self.fig_TOF, master = self.TOF_Frame)
        self.canvas_TOF.get_tk_widget().configure(background = 'white', highlightcolor = 'white', highlightbackground = 'white')
        self.plot_widget_TOF = self.canvas_TOF.get_tk_widget()
        plt.draw()
        self.plot_widget_TOF.pack()


    def update(self, B):

        plt.cla()
        plt.clf()
        plt.imshow(B, interpolation = 'none', cmap = 'jet_r')
        self.canvas_TOF.draw()

        self.master.update()