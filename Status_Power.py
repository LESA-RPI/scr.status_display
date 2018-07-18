from Tkinter import *
from pysnmp.entity.rfc3413.oneliner import cmdgen

class POWER:
    
    def __init__(self, master):

        self.master = master

        # Values
        self.vals = [StringVar() for i in range(5)]
        self.vals[0].set('RMS Current: mA')
        self.vals[1].set('RMS Voltage: V')
        self.vals[2].set('Active Power: W')
        self.vals[3].set('Apparent Power: W')
        self.vals[4].set('Power Factor: ')

        # Frames
        self.frame = LabelFrame(master, bg = 'white', text = 'Power Management', font = ("Helvetica", 16), width = 600, heigh = 200)
        self.frame.pack_propagate(0)
        self.frame.pack(fill = None, expand = False, side = LEFT, anchor = NW, padx = 10, pady = 10)
        self.values = Frame(self.frame, bg = 'white', bd = 0)
        self.values.pack(fill = None, expand = False, side = LEFT, anchor = W)
        
        # Labels
        self.labels = []
        for i in range(len(self.vals)):
            self.labels.append(Label(self.values, bg = 'white', font = ("Helvetica", 14), textvariable = self.vals[i] ))
            self.labels[i].pack(anchor = W)
        
    def update(self, C, V, Act, App, P):
        
        self.vals[0].set('  RMS Current: %s00 mA ' % C)
        self.vals[1].set('  RMS Voltage: %s V'     % V)
        self.vals[2].set('  Active Power: %s W'    % Act)
        self.vals[3].set('  Apparent Power: %s AV' % App)
        self.vals[4].set('  Power Factor: 0.%s'    % P)

        self.master.update()