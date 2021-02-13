from tkinter import *
import board
import option

root = Tk()
grid_point = []
l = []
po = []
grid_circle = []
cur = []
editLines = []
editPoints = []
selected = None
interface_grid = board.Grid([50, 30])


def relevent_point(widget):
    widget.configure(bg="black")
    point = option.get_coordinates(interface_grid, widget)
    grid_point.append(board.Point(widget, point))


def clear_all(widget):
    for i in range(interface_grid.ysize):
        for j in range(interface_grid.xsize):
            widget[i][j].configure(bg="white")

    del grid_point[:]
    del l[:]
    del po[:]
    del grid_circle[:]
    del cur[:]
    global selected
    selected = None


def draw_line():
    generated_points = grid_point[-2].connect_points(grid_point[-1])

    line = []
    for point in generated_points:
        line.append(board.Point(matriz[point[1]][point[0]], point))

    # paint the points
    for point in line:
        point.widget.configure(bg='blue')


def draw_circle():

    r, generated_points = grid_point[-2].connect_circle(new_point=grid_point[-1])

    circle = []
    for point in generated_points:
        if 0 <= point[0] <= interface_grid.xsize - 1 and 0 <= point[1] <= interface_grid.ysize - 1:
            circle.append(board.Point(matriz[point[1]][point[0]], point))

    # paint the points used as reference
    grid_point[-2].widget.configure(bg='white')
    grid_point[-1].widget.configure(bg='white')

    # paint the circle
    for point in circle:
        point.widget.configure(bg='blue')

    # grid_circle.append(board.Circle(grid_point[-2], r, circle))

    # del grid_point[:]


# Frames
buttonFrame = Frame(root)
buttonFrame.grid(row=0, column=0, sticky=W, padx=5, pady=5)

gridFrame = Frame(root)
gridFrame.grid(row=1, column=0)

# Write Grid
matriz, linha = [], []
for i in range(interface_grid.ysize):
    for j in range(interface_grid.xsize):
        new_frame = Frame(gridFrame, bg="white", height=15, width=15, bd=1, relief=SUNKEN)
        new_frame.bind("<Button-1>", lambda event, widget=new_frame: relevent_point(widget))
        new_frame.grid(row=i, column=j)
        linha.append(new_frame)
    matriz.append(linha)
    linha = []

# Write Buttons
bresenham_button = Button(buttonFrame, text="Bresenham", command=lambda: draw_line())
bresenham_button.pack(side=LEFT, padx=5)

circulo = Button(buttonFrame, text="Circulo", command=lambda: draw_circle())
circulo.pack(side=LEFT, padx=5)

clear_button = Button(buttonFrame, text="Clear", fg="Red", command=lambda: clear_all(matriz))
clear_button.pack(side=RIGHT, padx=5)

root.mainloop()
