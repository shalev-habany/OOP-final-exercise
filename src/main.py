from src.canvas import Canvas
from src.shapes.line import Line
from src.shapes.point import Point
from src.shapes.triangle import Triangle

if __name__ == '__main__':

    canvas = Canvas(800, 800)
    line_color = (0, 255, 0)
    point1 = Point(100, 100, line_color, canvas.image)
    point2 = Point(200, 200, line_color, canvas.image)
    point3 = Point(300, 100, line_color, canvas.image)
    point4 = Point(100, 600, line_color, canvas.image)
    point5 = Point(200, 500, line_color, canvas.image)
    line1 = Line(point4, point5, line_color, canvas.image)
    triangle = Triangle(point1, point2, point3, line_color, canvas.image)
    triangle.translate(200, 200)
    triangle.rotate(180)
    triangle.scale(2)
    line1.scale(2)
    line1.translate(200,0)
    canvas.add_shape(triangle)
    canvas.add_shape(line1)
    canvas.draw()
    canvas.display()