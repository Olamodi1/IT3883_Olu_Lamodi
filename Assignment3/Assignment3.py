# Program Name: Assignment3.py
# Course: IT3883/Section W02
# Student Name: Olu Lamodi
# Assignment Number: Assignment 3
# Due Date: 06/26/2026
# Purpose: This program converts miles per gallon (mpg) into kilometers per
# liter (km/l) using a GUI. The answer updates automatically while you type,
# you dont have to click a button. It also wont crash if you type letters
# or leave the box empty, it just shows a message instead.
# Resources used: tkinter docs on python.org for the trace function,
# and the conversion number from the assignment sheet.

import tkinter as tk

# this is the function that runs every time the text box changes
def update_answer(*args):
    mpg_text = entry_box.get()

    # if they didnt type anything yet
    if mpg_text == "":
        answer_label.config(text="Enter a number above")
        return

    # try to convert it to a number, if it fails that means they typed
    # letters or something weird so just tell them instead of crashing
    try:
        mpg_num = float(mpg_text)
    except:
        answer_label.config(text="That's not a valid number")
        return

    km_l = mpg_num * 0.425143707
    answer_label.config(text=str(round(km_l, 4)) + " km/L")


# set up the window
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("350x180")

label1 = tk.Label(window, text="Enter MPG:")
label1.pack(pady=10)

# this variable is linked to the entry box so we can watch it for changes
mpg_var = tk.StringVar()
entry_box = tk.Entry(window, textvariable=mpg_var)
entry_box.pack()

# this is what calls update_answer automatically every time you type
mpg_var.trace("w", update_answer)

answer_label = tk.Label(window, text="Enter a number above", font=("Arial", 14))
answer_label.pack(pady=20)

note_label = tk.Label(window, text="(1 mpg = 0.425143707 km/L)", fg="gray")
note_label.pack()

window.mainloop()