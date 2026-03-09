from tkinter import *
from tkinter import ttk

def generate():
    return 'generate'

root = Tk()

root.title('Password Generator')
mainframe = ttk.Frame(root, padding=(3,3,12,12))
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

#input len
length = StringVar()
length_entry = ttk.Entry(mainframe, width=7, textvariable=length)
length_entry.grid(column=2,row=1,sticky=(W,E))

res = StringVar()

#ttk.Label(mainframe, textvariable=res).grid(column=2, row=1, sticky=(W,E))
ttk.Button(mainframe, text='generate', command=generate).grid(column=3, row=5, sticky= W)
ttk.Label(mainframe, text='password length').grid(column=3, row=1,sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

length_entry.focus()
root.bind("<Return>", generate)

root.mainloop()
