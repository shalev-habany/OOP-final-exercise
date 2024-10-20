import cv2
import numpy as np
from numpy import ndarray

from src.shapes.line import Line
from src.shapes.point import Point
from src.shapes.shape import Shape
from src.transform_shapes.transform_shapes import TransformShape


class Rectangle(Shape, TransformShape):
    def __init__(self, center: Point, width: float, height: float, line_color: tuple[float, float, float],
                 image: ndarray):
        self.width = width
        self.height = height
        self.center = center
        self.line_color = line_color
        self.image = image
        self.top_left = Point(center.x - width / 2, center.y - height / 2, line_color, image)
        self.top_right = Point(center.x + width / 2, center.y - height / 2, line_color, image)
        self.bottom_left = Point(center.x - width / 2, center.y + height / 2, line_color, image)
        self.bottom_right = Point(center.x + width / 2, center.y + height / 2, line_color, image)
        self.top_line, self.right_line, self.bottom_line, self.left_line = self.create_lines_from_points()

    def draw(self) -> None:
        self.top_line.draw()
        self.right_line.draw()
        self.bottom_line.draw()
        self.left_line.draw()

    def create_lines_from_points(self):
        top_line = Line(self.top_left, self.top_right, self.line_color, self.image)
        right_line = Line(self.top_right, self.bottom_right, self.line_color, self.image)
        bottom_line = Line(self.bottom_right, self.bottom_left, self.line_color, self.image)
        left_line = Line(self.bottom_left, self.top_left, self.line_color, self.image)
        return top_line, right_line, bottom_line, left_line

    def translate(self, x_offset: float, y_offset: float) -> None:
        super().translate_shape(x_offset, y_offset,
                                [self.top_left, self.top_right, self.bottom_left, self.bottom_right])

    def rotate(self, angle: float) -> None:
        super().rotate_shape(angle, self.center, [self.top_left, self.top_right, self.bottom_left, self.bottom_right])

    def scale(self, factor: float) -> None:
        super().scale_shape(factor, self.center, [self.top_left, self.top_right, self.bottom_left, self.bottom_right])

    def update_center(self) -> None:
        self.center.set_point((self.top_left.x + self.top_right.x) / 2,
                              (self.top_left.y + self.bottom_left.y) / 2)

    def get_points_list(self) -> list[Point]:
        return [self.top_left, self.top_right, self.bottom_left, self.bottom_right]

    def get_center(self) -> Point:
        return self.center
