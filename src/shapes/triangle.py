import cv2
import numpy as np

from src.shapes.point import Point
from src.shapes.shape import Shape
from src.shapes.line import Line
from src.transform_shapes.transform_shapes import TransformShape


class Triangle(Shape, TransformShape):
    def __init__(self, point1: Point, point2: Point, point3: Point, line_color, image):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.line_color = line_color
        self.image = image
        center_x = (self.point1.x + self.point2.x + self.point3.x) / 3
        center_y = (self.point1.y + self.point2.y + self.point3.y) / 3
        self.center = Point(center_x, center_y, line_color, image)
        self.line1, self.line2, self.line3 = self.create_lines_from_points()

    def create_lines_from_points(self):
        line1 = Line(self.point1, self.point2, self.line_color, self.image)
        line2 = Line(self.point2, self.point3, self.line_color, self.image)
        line3 = Line(self.point3, self.point1, self.line_color, self.image)
        return line1, line2, line3

    def draw(self) -> None:
        self.line1.draw()
        self.line2.draw()
        self.line3.draw()

    def rotate(self, angle: float) -> None:
        super().rotate_shape(angle, self.center, [self.point1, self.point2, self.point3])

    def scale(self, factor: float) -> None:
        super().scale_shape(factor, self.center, [self.point1, self.point2, self.point3])

    def translate(self, x_offset: float, y_offset: float) -> None:
        super().translate_shape(x_offset, y_offset, [self.point1, self.point2, self.point3])

    def update_center(self):
        self.center.set_point((self.point1.x + self.point2.x + self.point3.x) / 3,
                              (self.point1.y + self.point2.y + self.point3.y) / 3)
