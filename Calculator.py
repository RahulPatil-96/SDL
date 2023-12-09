import tkinter as tk
from tkinter import *

app = tk.Tk()
app.geometry("250x300")
app.title("Python Calculator")
app.maxsize(250, 300)
app.minsize(250, 300)

ent = Entry(app, width=16, borderwidth=3, relief=RIDGE)
ent.grid(pady=10, row=0, column=0, columnspan=4, padx=15)

# Function to update entry widget
def button_click(number):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(current) + str(number))

# Function to clear the entry widget
def button_clear():
    ent.delete(0, END)

# Function to perform calculation
def button_equal():
    try:
        result = eval(ent.get())
        ent.delete(0, END)
        ent.insert(0, result)
    except Exception as e:
        ent.delete(0, END)
        ent.insert(0, "Error")

# Create buttons for digits
for i in range(1, 10):
    btn = Button(app, text=str(i), padx=20, pady=20, command=lambda i=i: button_click(i))
    btn.grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3)

# Create button for zero
btn_zero = Button(app, text="0", padx=20, pady=20, command=lambda: button_click(0))
btn_zero.grid(row=4, column=1)

# Create arithmetic operation buttons
operations = ['+', '-', '*', '/']
for i, operation in enumerate(operations):
    btn = Button(app, text=operation, padx=20, pady=20, command=lambda op=operation: button_click(op))
    btn.grid(row=i + 1, column=3)

# Create clear and equal buttons
btn_clear = Button(app, text="C", padx=20, pady=20, command=button_clear)
btn_clear.grid(row=4, column=0)

btn_equal = Button(app, text="=", padx=20, pady=20, command=button_equal)
btn_equal.grid(row=4, column=2)

app.mainloop()
