import tkinter
from tkinter import *
from tkinter import ttk, messagebox

import secrets
from string import ascii_letters, digits, punctuation

bank = digits + ascii_letters +punctuation

def generate(*args):
    try:
        pl = int(pass_len.get())

        if pl <= 0:
            raise ValueError

        gp = ''
        for x in range(pl):
            gp += secrets.choice(bank)

        #print("ran")
        generated_pass.set(gp)

    except ValueError:
        messagebox.showerror('Invalid value','must enter a whole number greater than 0')


root = Tk()
root.title("Password Generator")

mainframe = ttk.Frame(root)
mainframe.grid(column=2)

#length entry
pass_len = StringVar()
pass_len_entry = ttk.Entry(mainframe,textvariable=pass_len)
pass_len_entry.grid()
ttk.Label(mainframe, text="len").grid()


#button
generated_pass = StringVar()
ttk.Button(mainframe,text="generate",command=generate).grid()
ttk.Entry(mainframe,textvariable=generated_pass).grid() #entry so user can edit and copy password

#run program
root.mainloop()