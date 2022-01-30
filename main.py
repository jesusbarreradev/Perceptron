import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
# from tkinter.ttk import *
import matplotlib

matplotlib.use("TkAgg")


def display_coordinates(event):
    my_label["text"] = f'x={event.x} y={event.y}'


def handle_init_weights():
    return


def handle_init_perceptron():
    return


def handle_init_evaluation():
    return


# TK Window
root = Tk()
root.geometry('600x300')
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
my_label = tkinter.Label(relief="solid", font="Times 22 bold")
# Displaying canvas and label
# canvas.get_tk_widget().grid(row=0, column=0)
canvas.get_tk_widget().place(x=0, y=0)
canvas.get_tk_widget().bind('<Button-1>', display_coordinates)
my_label.place(x=420, y=20)
# Weights button
initWeights = tkinter.Button(bg="white", text="Iniciar pesos",
                             command=handle_init_weights)
initWeights.place(x=420, y=100)
# Perceptron button
initPerceptron = tkinter.Button(bg="white", text="Entrenar perceptron",
                                command=handle_init_perceptron)
initPerceptron.place(x=420, y=150)
# Evaluate button
initEvaluation = tkinter.Button(bg="white", text="Evaluar resultado",
                                command=handle_init_evaluation)
initEvaluation.place(x=420, y=200)
# Run mainloop
root.mainloop()
