from tkinter import *
import time
from datetime import datetime, timedelta
from tkinter import ttk,messagebox

is_running = True
end_time = None
remaining= None

def set_countdown():
    global end_time
    end_time= datetime.now() + timedelta(minutes = 5)
    update()


def update():
    global remaining
    remaining = end_time - datetime.now()

    if is_running:
        if remaining.total_seconds() <= 0:
            timer_var.set('00:00')
            break_indicator.set("On break")
            return

        mins, secs = divmod(int(remaining.total_seconds()), 60)
        timer_var.set(f"{mins:02}:{secs:02}")

        root.after(1000, update)


def pause():
    global is_running
    is_running = not is_running

    if is_running:
        #resume
        update()

    else:
        #pause and save remaining time
        global end_time
        end_time = datetime.now() + remaining




root = Tk()

mainframe = ttk.Frame(root)
mainframe.grid()

timer_var = StringVar(value="25:00")

ttk.Label(mainframe,textvariable=timer_var).grid()
ttk.Button(mainframe,text="start",command=set_countdown).grid()


break_indicator =StringVar(value = "not on break")
ttk.Label(mainframe,textvariable= break_indicator).grid()

is_paused = StringVar(value="Pause")
ttk.Button(mainframe, textvariable=is_paused, command=pause).grid()

root.mainloop()
#x = datetime.datetime.now()
