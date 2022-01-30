from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter.ttk import *
import matplotlib
matplotlib.use("TkAgg")

def define_txt(root):
    miFrame= Frame(root, width=400, height= 400)
    #miFrame.pack()

    cuadro=Entry(miFrame)
    cuadro.place(x=90,y=30)

def define_labels():
    label_theta= Label(text="Valor theta",font=("Verdana",10)).place(x=10,y=10)


def display_coordinates(event):
    my_label["text"] = f'x={event.x} y={event.y}'


def interface(root):
    # TK Window
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
    define_labels()
   
    #define_txt(root)


    # Displaying canvas and label
    canvas.get_tk_widget().grid(row=0, column=0)
    canvas.get_tk_widget().bind('<Button-1>', display_coordinates)
    my_label.grid(row=0, column=1)

def run():
     # Run mainloop
    root = Tk()
    interface(root)
    root.mainloop()

if __name__ == '__main__':
    run()