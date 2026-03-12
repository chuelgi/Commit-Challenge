from tkinter import *
import time
from datetime import datetime, timedelta
from tkinter import ttk,messagebox

def set_countdown():
    start_time = datetime.now()
    end_time = start_time+ timedelta(minutes = 5)

    def update():
        now = datetime.now()
        remaining = end_time - now


    return

root = Tk()

mainframe = ttk.Frame(root)
mainframe.grid()

x = datetime.now().time()

ttk.Label(mainframe,text=x).grid()
ttk.Button(mainframe,text="start",command=set_countdown)

root.mainloop()
#x = datetime.datetime.now()
print(x)
