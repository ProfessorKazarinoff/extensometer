#!/usr/bin/env python

import tkinter as tk

window = tk.Tk()
window.geometry('350x200')

window.title("Welcome to the extensometer app")

lbl = tk.Label(window, text="Hello",  font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

btn = tk.Button(window, text="Click Me", bg="blue", fg="white")
btn.grid(column=0, row=2)

window.mainloop()