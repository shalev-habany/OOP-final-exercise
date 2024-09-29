import cv2
import numpy as np
from numpy import ndarray

from src.shapes.point import Point
from src.shapes.shape import Shape


class Line(Shape):

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

    def rotate(self, angle: int) -> None:
        rotation_matrix = cv2.getRotationMatrix2D((self.center.x, self.center.y), angle, 1)
        self.apply_operation_matrix(rotation_matrix)

    def translate(self, x_offset: int, y_offset: int) -> None:
        self.point1.translate(x_offset, y_offset)
        self.point2.translate(x_offset, y_offset)
        self.update_center()

    def scale(self, factor: float) -> None:
        scale_matrix = cv2.getRotationMatrix2D((self.center.x, self.center.y), 0, factor)
        self.apply_operation_matrix(scale_matrix)

    def apply_operation_matrix(self, matrix: ndarray) -> None:
        point1_scaled = matrix @ np.array([[self.point1.x], [self.point1.y], [1]])
        point2_scaled = matrix @ np.array([[self.point2.x], [self.point2.y], [1]])
        self.point1.set_point(point1_scaled[0, 0], point1_scaled[1, 0])
        self.point2.set_point(point2_scaled[0, 0], point2_scaled[1, 0])

    def update_center(self) -> None:
        self.center.set_point((self.point1.x + self.point2.x) / 2,
                              (self.point1.y + self.point2.y) / 2)
