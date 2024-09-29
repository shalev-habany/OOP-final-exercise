import cv2
from numpy import ndarray

from src.shapes.point import Point
from src.shapes.shape import Shape


class Circle(Shape):
    def __init__(self, radius, center: Point, line_color: tuple[int, int, int], image: ndarray):
        self.center = center
        self.radius = radius
        self.line_color = line_color
        self.image = image

    def draw(self) -> None:
        cv2.circle(self.image, (int(self.center.x), int(self.center.y)), int(self.radius), self.line_color)

    def translate(self, x_offset: float, y_offset: float) -> None:
        self.center.translate(x_offset, y_offset)

    def rotate(self, angle: float) -> None:
        pass

    def scale(self, factor: float) -> None:
        self.radius *= factor
