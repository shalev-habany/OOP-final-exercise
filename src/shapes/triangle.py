import cv2
import numpy as np

from src.shapes.point import Point
from src.shapes.shape import Shape
from src.shapes.line import Line


class Triangle(Shape):
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

    def rotate(self, angle: int) -> None:
        rotation_matrix = cv2.getRotationMatrix2D((self.center.x, self.center.y), angle, 1)
        self.apply_operation_matrix(rotation_matrix)

    def scale(self, factor: float) -> None:
        scale_matrix = cv2.getRotationMatrix2D((self.center.x, self.center.y), 0, factor)
        self.apply_operation_matrix(scale_matrix)

    def translate(self, x_offset: int, y_offset: int) -> None:
        self.point1.translate(x_offset, y_offset)
        self.point2.translate(x_offset, y_offset)
        self.point3.translate(x_offset, y_offset)
        self.update_center()

    def apply_operation_matrix(self, matrix):
        point1_scaled = matrix @ np.array([[self.point1.x], [self.point1.y], [1]])
        point2_scaled = matrix @ np.array([[self.point2.x], [self.point2.y], [1]])
        point3_scaled = matrix @ np.array([[self.point3.x], [self.point3.y], [1]])
        self.point1.set_point(point1_scaled[0, 0], point1_scaled[1, 0])
        self.point2.set_point(point2_scaled[0, 0], point2_scaled[1, 0])
        self.point3.set_point(point3_scaled[0, 0], point3_scaled[1, 0])

    def update_center(self):
        self.center.set_point((self.point1.x + self.point2.x + self.point3.x) / 3,
                              (self.point1.y + self.point2.y + self.point3.y) / 3)
