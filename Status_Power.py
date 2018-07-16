from Tkinter import *
from pysnmp.entity.rfc3413.oneliner import cmdgen

class POWER:
    def __init__(self, master):
        self.master = master
        self.val_A = StringVar()
        self.val_V  = StringVar()
        self.val_W  = StringVar()
        self.val_AV = StringVar()
        self.val_PF = StringVar()

        self.val_A.set('RMS Current: mA')
        self.val_V.set('RMS Voltage: V')
        self.val_W.set('Active Poewr: W')
        self.val_AV.set('Apparent Power: W')
        self.val_PF.set('Power Factor: ')

        self.frame = LabelFrame(master, bg = 'white', text = 'Power Management', font = ("Helvetica", 16), width = 600, heigh = 200)
        self.frame.pack_propagate(0)
        self.frame.pack(fill = None, expand = False, side = LEFT, anchor = NW, padx = 10, pady = 10)

        self.values = Frame(self.frame, bg = 'white', bd = 0)
        self.values.pack(fill = None, expand = False, side = LEFT, anchor = W)
        
        self.label_A  = Label(self.values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_A )
        self.label_V  = Label(self.values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_V )
        self.label_W  = Label(self.values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_W )
        self.label_AV = Label(self.values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_AV)
        self.label_PF = Label(self.values, bg = 'white', font = ("Helvetica", 14), textvariable = self.val_PF)

        self.label_A.pack(anchor = W)
        self.label_V.pack(anchor = W)
        self.label_W.pack(anchor = W)
        self.label_AV.pack(anchor = W)
        self.label_PF.pack(anchor = W)
        
    def update(self, C, V, Act, App, P):
        self.val_A.set( '  RMS Current: %s00 mA ' % C)
        self.val_V.set( '  RMS Voltage: %s V'     % V)
        self.val_W.set( '  Active Power: %s W'    % Act)
        self.val_AV.set('  Apparent Power: %s AV' % App)
        self.val_PF.set('  Power Factor: 0.%s'    % P)

        self.master.update()