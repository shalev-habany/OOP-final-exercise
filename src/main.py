from src.canvas import Canvas
from src.shapes.circle import Circle
from src.shapes.complex_shape import ComplexShape
from src.shapes.line import Line
from src.shapes.point import Point
from src.shapes.rectangle import Rectangle
from src.shapes.triangle import Triangle


def add_line(point1, point2, line_color, canvas):
    line = Line(point1, point2, line_color, canvas.image)
    canvas.add_shape(line)


def add_rectangle(center, width, height, line_color, canvas):
    rectangle = Rectangle(center, width, height, line_color, canvas.image)
    # canvas.add_shape(rectangle)
    return rectangle


def add_triangle(point1, point2, point3, line_color, canvas):
    triangle = Triangle(point1, point2, point3, line_color, canvas.image)
    # canvas.add_shape(triangle)
    return triangle


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
    # add_line(Point(100, 100, line_color, canvas.image), Point(200, 200, line_color, canvas.image), line_color, canvas)
    rect = add_rectangle(Point(400, 400, line_color, canvas.image), 100, 100, line_color, canvas)
    tri = add_triangle(Point(350, 350, line_color, canvas.image), Point(450, 350, line_color, canvas.image),
                 Point(400, 250, line_color, canvas.image), line_color, canvas)
    door = add_rectangle(Point(400, 425, line_color, canvas.image), 20, 50, line_color, canvas)
    complex_shape = ComplexShape([rect, tri, door], line_color, canvas.image)
    complex_shape.rotate(45)
    complex_shape.scale(2)
    complex_shape.translate(100, 100)
    canvas.add_shape(complex_shape)
    # add_circle(50, Point(400, 200, line_color, canvas.image), line_color, canvas)
    # rotate_everything(canvas, 45)
    # scale_everything(canvas, 1.5)
    # translate_everything(canvas, 100, 100)
    canvas.draw()
    canvas.display()
