from typing import Tuple

import cv2
from numpy import ndarray

from src.shapes.point import Point
from src.shapes.shape import Shape


class Circle(Shape):
    """
    A class representing a circle shape.
    """

    def __init__(self, radius: float, center: Point, line_color: Tuple[float, float, float]):
        """
        Initialize a Circle instance.

        :param radius: The radius of the circle.
        :param center: The center point of the circle.
        :param line_color: The color of the circle's line.
        """
        self.center = center
        self.radius = radius
        self.line_color = line_color

    def draw(self, image: ndarray) -> ndarray:
        """
        Draw the circle on the given image.

        :param image: The image on which to draw the circle.
        :return: The image with the circle drawn on it.
        """
        cv2.circle(image, (int(self.center.x), int(self.center.y)), int(self.radius), self.line_color)
        return image

    def translate(self, x_offset: float, y_offset: float) -> None:
        """
        Translate the circle by the given offsets.

        :param x_offset: The offset in the x direction.
        :param y_offset: The offset in the y direction.
        """
        self.center.translate(x_offset, y_offset)

    def rotate(self, angle: float) -> None:
        """
        Rotate the circle by the given angle. (No-op for circles)

        :param angle: The angle to rotate the circle by.
        """
        pass

    def scale(self, factor: float) -> None:
        """
        Scale the circle by the given factor.

        :param factor: The factor to scale the circle by.
        """
        self.radius *= factor

    def get_center(self) -> Point:
        """
        Get the center point of the circle.

        :return: The center point of the circle.
        """
        return self.center

    def get_points_list(self) -> list[Point]:
        """
        Get a list of points defining the circle.

        :return: A list containing the center point of the circle.
        """
        return [self.center]