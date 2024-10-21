import cv2
import numpy as np
from numpy import ndarray

from src.shapes.point import Point
from src.shapes.shape import Shape
from src.shapes.line import Line
from src.transform_shapes.transform_shapes import TransformShape


class Triangle(Shape, TransformShape):
    """
    A class representing a triangle shape.
    """

    def __init__(self, point1: Point, point2: Point, point3: Point, line_color: tuple[float, float, float]):
        """
        Initialize a Triangle instance.

        :param point1: The first point of the triangle.
        :param point2: The second point of the triangle.
        :param point3: The third point of the triangle.
        :param line_color: The color of the triangle's lines.
        """
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.line_color = line_color
        center_x = (self.point1.x + self.point2.x + self.point3.x) / 3
        center_y = (self.point1.y + self.point2.y + self.point3.y) / 3
        self.center = Point(center_x, center_y, line_color)
        self.line1, self.line2, self.line3 = self.create_lines_from_points()

    def create_lines_from_points(self) -> tuple[Line, Line, Line]:
        """
        Create lines from the triangle's corner points.

        :return: A tuple containing the three lines of the triangle.
        """
        line1 = Line(self.point1, self.point2, self.line_color)
        line2 = Line(self.point2, self.point3, self.line_color)
        line3 = Line(self.point3, self.point1, self.line_color)
        return line1, line2, line3

    def draw(self, image: ndarray) -> ndarray:
        """
        Draw the triangle on the given image.

        :param image: The image on which to draw the triangle.
        :return: The image with the triangle drawn on it.
        """
        self.line1.draw(image)
        self.line2.draw(image)
        self.line3.draw(image)
        return image

    def rotate(self, angle: float) -> None:
        """
        Rotate the triangle by the given angle.

        :param angle: The angle to rotate the triangle by.
        """
        super().rotate_shape(angle, self.center, [self.point1, self.point2, self.point3])

    def scale(self, factor: float) -> None:
        """
        Scale the triangle by the given factor.

        :param factor: The factor to scale the triangle by.
        """
        super().scale_shape(factor, self.center, [self.point1, self.point2, self.point3])

    def translate(self, x_offset: float, y_offset: float) -> None:
        """
        Translate the triangle by the given offsets.

        :param x_offset: The offset in the x direction.
        :param y_offset: The offset in the y direction.
        """
        super().translate_shape(x_offset, y_offset, [self.point1, self.point2, self.point3])

    def update_center(self) -> None:
        """
        Update the center point of the triangle.
        """
        self.center.set_point((self.point1.x + self.point2.x + self.point3.x) / 3,
                              (self.point1.y + self.point2.y + self.point3.y) / 3)

    def get_points_list(self) -> list[Point]:
        """
        Get a list of points defining the triangle.

        :return: A list containing the three corner points of the triangle.
        """
        return [self.point1, self.point2, self.point3]

    def get_center(self) -> Point:
        """
        Get the center point of the triangle.

        :return: The center point of the triangle.
        """
        return self.center
