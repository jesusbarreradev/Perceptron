# Press the green button in the gutter to run the script.
from tkinter import *


def display_coordinates(event):
    my_label["text"] = f'x={event.x} y={event.y}'


if __name__ == '__main__':
    my_window = Tk()
    my_window.geometry("800x400")
    my_canvas = Canvas(my_window, width=400, height=400, background='white')
    my_canvas.pack()
    my_label = Label(bd=4, relief="solid", font="Times 22 bold", bg="white", fg="black")
    my_canvas.bind('<Button-1>', display_coordinates)
    my_canvas.grid(row=0, column=0)
    my_label.grid(row=0, column=1)
    my_window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
