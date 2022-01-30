from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter.ttk import *
import matplotlib
matplotlib.use("TkAgg")


def display_coordinates(event):
    my_label["text"] = f'x={event.x} y={event.y}'


# TK Window
root = Tk()
# Creating figure
figure = Figure(figsize=(5, 4), dpi=100)
plot = figure.add_subplot(1, 1, 1)
plot.axis([-1, 1, -1, 1])
# adding vertical line in data co-ordinates
plot.axvline(0, c='black', ls='--')
# adding horizontal line in data co-ordinates
plot.axhline(0, c='black', ls='--')
# Creating canvas & label
canvas = FigureCanvasTkAgg(figure, root)
my_label = Label(relief="solid", font="Times 22 bold")
# Displaying canvas and label
canvas.get_tk_widget().grid(row=0, column=0)
canvas.get_tk_widget().bind('<Button-1>', display_coordinates)
my_label.grid(row=0, column=1)
# Run mainloop
root.mainloop()
