import math


def get_coordinates(grid, point):

    point = str(point)

    if len(point) == 15:
        point = [0, 0]

    else:
        point = int(point[15:])

        if point % grid.xsize == 0:
            x_coord = grid.xsize -1
            y_coord = 1
        else:
            x_coord = point % grid.xsize - 1
            y_coord = 0

        point = [x_coord, point // grid.xsize - y_coord]
    return point


def interpol(p1, p2, t):
    inter = []
    for i in range(2):
        inter.append((1-t)*p1[i] + t*p2[i])

    return inter


def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def m(p1, p2):
    if p2[0] == p1[0]:
        m = 0
    else:
        m = (p2[1]-p1[1])/(p2[0]-p1[0])

    return m