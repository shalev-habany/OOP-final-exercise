import cv2
import numpy as np
from numpy import ndarray

from src.shapes.point import Point
from src.shapes.shape import Shape
from src.transform_shapes.transform_shapes import TransformShape


class Line(Shape, TransformShape):

    def __init__(self, point1: Point, point2: Point, line_color, image):
        self.point1 = point1
        self.point2 = point2
        self.line_color = line_color
        self.image = image
        center_x = (self.point1.x + self.point2.x) / 2
        center_y = (self.point1.y + self.point2.y) / 2
        self.center = Point(center_x, center_y, line_color, image)

    def draw(self) -> None:
        cv2.line(self.image, (int(self.point1.x), int(self.point1.y)), (int(self.point2.x), int(self.point2.y)),
                 self.line_color, 1)

    def rotate(self, angle: float) -> None:
        super().rotate_shape(angle, self.center, [self.point1, self.point2])

    def translate(self, x_offset: float, y_offset: float) -> None:
        super().translate_shape(x_offset, y_offset, [self.point1, self.point2])

    def scale(self, factor: float) -> None:
        super().scale_shape(factor, self.center, [self.point1, self.point2])

    def update_center(self) -> None:
        self.center.set_point((self.point1.x + self.point2.x) / 2,
                              (self.point1.y + self.point2.y) / 2)

    def get_points_list(self) -> list[Point]:
        return [self.point1, self.point2]

    def get_center(self):
        return self.center
