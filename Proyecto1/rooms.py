#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 16, 2020 11:42:36 PM CST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import rooms_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    rooms_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    rooms_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("500x500+662+231")
        top.minsize(1, 1)
        top.maxsize(3825, 1050)
        top.resizable(1, 1)
        top.title("Seleccion de salas")
        top.configure(background="#556B2F")
        top.configure(highlightcolor="black")

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.54, rely=0.182, height=81, width=191)
        self.Button1_1.configure(activebackground="#f8e5b7")
        self.Button1_1.configure(background="#f8e5b7")
        self.Button1_1.configure(text='''2''')

        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(relx=0.08, rely=0.182, height=81, width=191)
        self.Button1_2.configure(activebackground="#89cff0")
        self.Button1_2.configure(background="#89cff0")
        self.Button1_2.configure(cursor="fleur")
        self.Button1_2.configure(text='''1''')

        self.Button1_3 = tk.Button(top)
        self.Button1_3.place(relx=0.08, rely=0.47, height=81, width=191)
        self.Button1_3.configure(activebackground="#d9f4ed")
        self.Button1_3.configure(background="#d9f4ed")
        self.Button1_3.configure(text='''3''')

        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(relx=0.54, rely=0.47, height=81, width=191)
        self.Button1_2.configure(activebackground="#ffcccb")
        self.Button1_2.configure(background="#ffcccb")
        self.Button1_2.configure(text='''4''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.24, rely=0.08, height=21, width=258)
        self.Label1.configure(background="#556B2F")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Seleccionar la sala donde se va a jugar''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.38, rely=0.74, height=31, width=124)
        self.Button1.configure(text='''Menu principal''')

if __name__ == '__main__':
    vp_start_gui()





