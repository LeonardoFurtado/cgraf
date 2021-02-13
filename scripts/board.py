import algorithms
import math


class Grid:

    def __init__(self, grid):
        self.xsize = grid[0]
        self.ysize = grid[1]
        self.matriz = None

    def define_matrix(self, matriz):
        self.matriz = matriz


class Point:

    def __init__(self, widget, point):
        self.x = point[0]
        self.y = point[1]
        self.point = point
        self.widget = widget

    def connect_points(self, new_point):
        return algorithms.bresenham([self.x, self.y], [new_point.x, new_point.y])

    def connect_circle(self, new_point=None, radius=None):
        if new_point:
            return algorithms.circle([self.x, self.y], final_pixel=[new_point.x, new_point.y])
        elif radius:
            return algorithms.circle([self.x, self.y], r=radius)

    def move_point(self, new_point, matriz):
        self.point[0], self.point[1] = int(self.point[0] + new_point[0]), int(self.point[1] + new_point[1])
        self.x = self.point[0]
        self.y = self.point[1]
        self.widget = matriz[self.point[1]][self.point[0]]


class Line:

    def __init__(self, line):
        self.point1 = line[0]
        self.point2 = line[-1]
        self.points = line

    def update(self, line):
        self.point1 = line[0]
        self.point2 = line[-1]
        self.points = line

    def del_first(self):
        self.points.pop(0)


class Circle:

    def __init__(self, center: Point, r, circunference):
        self.center = center
        self.radius = r
        self.points = circunference

    def translade(self, points, matriz):

        self.center.move_point(points, matriz)

        generated = self.center.connect_circle(radius = self.radius)
        transladed = []

        for point in generated:
            transladed.append(Point(matriz[point[1]][point[0]], point))

        self.points = transladed

    def escale(self, escale, matriz):

        self.radius = math.floor(self.radius*escale)

        generated = self.center.connect_circle(radius = self.radius)
        escalated = []

        for point in generated:
            escalated.append(Point(matriz[point[1]][point[0]], point))

        self.points = escalated






