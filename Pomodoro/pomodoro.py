from tkinter import *
import time
from datetime import datetime, timedelta
from tkinter import ttk,messagebox

def set_countdown():
    end_time = datetime.now() + timedelta(minutes = 25)

    def update():
        remaining = end_time - datetime.now()

        if remaining.total_seconds() <= 0:
            timer_var.set('00:00')
            return

        mins, secs = divmod(int(remaining.total_seconds()),60)
        timer_var.set(f"{mins:02}:{secs:02}")

        root.after(1000, update)

    update()


    return

root = Tk()

mainframe = ttk.Frame(root)
mainframe.grid()

timer_var = StringVar(value="25:00")

ttk.Label(mainframe,textvariable=timer_var).grid()
ttk.Button(mainframe,text="start",command=set_countdown).grid()

ttk.Button(mainframe, text="pasue").grid()

root.mainloop()
#x = datetime.datetime.now()
