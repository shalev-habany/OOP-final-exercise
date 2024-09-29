from src.canvas import Canvas
from src.shapes.circle import Circle
from src.shapes.line import Line
from src.shapes.point import Point
from src.shapes.rectangle import Rectangle
from src.shapes.triangle import Triangle


def add_line(point1, point2, line_color, canvas):
    line = Line(point1, point2, line_color, canvas.image)
    canvas.add_shape(line)


def add_rectangle(center, width, height, line_color, canvas):
    rectangle = Rectangle(center, width, height, line_color, canvas.image)
    canvas.add_shape(rectangle)


def add_triangle(point1, point2, point3, line_color, canvas):
    triangle = Triangle(point1, point2, point3, line_color, canvas.image)
    canvas.add_shape(triangle)


def add_circle(radius, center, line_color, canvas):
    circle = Circle(radius, center, line_color, canvas.image)
    canvas.add_shape(circle)

def rotate_everything(canvas, angle):
    for shape in canvas.shapes:
        shape.rotate(angle)

def scale_everything(canvas, factor):
    for shape in canvas.shapes:
        shape.scale(factor)

def translate_everything(canvas, x_offset, y_offset):
    for shape in canvas.shapes:
        shape.translate(x_offset, y_offset)

if __name__ == '__main__':
    canvas = Canvas(800, 800)
    line_color = (0, 255, 0)
    add_line(Point(100, 100, line_color, canvas.image), Point(200, 200, line_color, canvas.image), line_color, canvas)
    add_rectangle(Point(400, 400, line_color, canvas.image), 100, 100, line_color, canvas)
    add_triangle(Point(100, 200, line_color, canvas.image), Point(200, 200, line_color, canvas.image),
                 Point(150, 100, line_color, canvas.image), line_color, canvas)
    add_circle(50, Point(400, 200, line_color, canvas.image), line_color, canvas)
    rotate_everything(canvas, 45)
    scale_everything(canvas, 1.5)
    translate_everything(canvas, 100, 100)
    canvas.draw()
    canvas.display()
