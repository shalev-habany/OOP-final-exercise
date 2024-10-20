from numpy import ndarray

from src.shapes.shape import Shape
import cv2


class Point(Shape):

    def __init__(self, x: float, y: float, line_color: tuple[float, float, float], image: ndarray):
        self.x = x
        self.y = y
        self.line_color = line_color
        self.image = image

    def draw(self) -> None:
        cv2.circle(self.image, (int(self.x), int(self.y)), 1, self.line_color, -1)

    def rotate(self, angle) -> None:
        pass

    def translate(self, x_offset, y_offset) -> None:
        self.x += x_offset
        self.y += y_offset

    def scale(self, factor) -> None:
        pass

    def set_point(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_points_list(self):
        return [self]

    def get_center(self):
        return self
