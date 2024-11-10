from typing import Tuple

import cv2
import numpy as np
from numpy import ndarray

from src.shapes.point import Point
from src.shapes.shape import Shape
from src.transform_shapes.transform_shapes import TransformShape


class Line(Shape):
    """
    A class representing a line shape.
    """

    def __init__(self, point1: Point, point2: Point, line_color: Tuple[float, float, float]):
        """
        Initialize a Line instance.

        :param point1: The starting point of the line.
        :param point2: The ending point of the line.
        :param line_color: The color of the line.
        """
        self.point1 = point1
        self.point2 = point2
        self.line_color = line_color
        center_x = (self.point1.x + self.point2.x) / 2
        center_y = (self.point1.y + self.point2.y) / 2
        self.center = Point(center_x, center_y, line_color)

    def draw(self, image: ndarray) -> ndarray:
        """
        Draw the line on the given image.

        :param image: The image on which to draw the line.
        :return: The image with the line drawn on it.
        """
        cv2.line(image, (int(self.point1.x), int(self.point1.y)), (int(self.point2.x), int(self.point2.y)),
                 self.line_color, 1)
        return image

    def rotate(self, angle: float) -> None:
        """
        Rotate the line by the given angle.

        :param angle: The angle to rotate the line by.
        """
        TransformShape.rotate_shape(angle, self.center, [self.point1, self.point2])

    def translate(self, x_offset: float, y_offset: float) -> None:
        """
        Translate the line by the given offsets.

        :param x_offset: The offset in the x direction.
        :param y_offset: The offset in the y direction.
        """
        TransformShape.translate_shape(self, x_offset, y_offset, [self.point1, self.point2])

    def scale(self, factor: float) -> None:
        """
        Scale the line by the given factor.

        :param factor: The factor to scale the line by.
        """
        TransformShape.scale_shape(factor, self.center, [self.point1, self.point2])

    def update_center(self) -> None:
        """
        Update the center point of the line.
        """
        self.center.set_point((self.point1.x + self.point2.x) / 2, (self.point1.y + self.point2.y) / 2)

    def get_points_list(self) -> list[Point]:
        """
        Get a list of points defining the line.

        :return: A list containing the starting and ending points of the line.
        """
        return [self.point1, self.point2]

    def get_center(self) -> Point:
        """
        Get the center point of the line.

        :return: The center point of the line.
        """
        return self.center
