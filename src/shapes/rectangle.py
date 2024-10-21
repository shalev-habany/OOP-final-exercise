import cv2
import numpy as np
from numpy import ndarray

from src.shapes.line import Line
from src.shapes.point import Point
from src.shapes.shape import Shape
from src.transform_shapes.transform_shapes import TransformShape


class Rectangle(Shape, TransformShape):
    """
    A class representing a rectangle shape.
    """

    def __init__(self, center: Point, width: float, height: float, line_color: tuple[float, float, float]):
        """
        Initialize a Rectangle instance.

        :param center: The center point of the rectangle.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param line_color: The color of the rectangle's lines.
        """
        self.width = width
        self.height = height
        self.center = center
        self.line_color = line_color
        self.top_left = Point(center.x - width / 2, center.y - height / 2, line_color)
        self.top_right = Point(center.x + width / 2, center.y - height / 2, line_color)
        self.bottom_left = Point(center.x - width / 2, center.y + height / 2, line_color)
        self.bottom_right = Point(center.x + width / 2, center.y + height / 2, line_color)
        self.top_line, self.right_line, self.bottom_line, self.left_line = self.create_lines_from_points()

    def draw(self, image: ndarray) -> ndarray:
        """
        Draw the rectangle on the given image.

        :param image: The image on which to draw the rectangle.
        :return: The image with the rectangle drawn on it.
        """
        self.top_line.draw(image)
        self.right_line.draw(image)
        self.bottom_line.draw(image)
        self.left_line.draw(image)
        return image

    def create_lines_from_points(self) -> tuple[Line, Line, Line, Line]:
        """
        Create lines from the rectangle's corner points.

        :return: A tuple containing the four lines of the rectangle.
        """
        top_line = Line(self.top_left, self.top_right, self.line_color)
        right_line = Line(self.top_right, self.bottom_right, self.line_color)
        bottom_line = Line(self.bottom_right, self.bottom_left, self.line_color)
        left_line = Line(self.bottom_left, self.top_left, self.line_color)
        return top_line, right_line, bottom_line, left_line

    def translate(self, x_offset: float, y_offset: float) -> None:
        """
        Translate the rectangle by the given offsets.

        :param x_offset: The offset in the x direction.
        :param y_offset: The offset in the y direction.
        """
        super().translate_shape(x_offset, y_offset,
                                [self.top_left, self.top_right, self.bottom_left, self.bottom_right])

    def rotate(self, angle: float) -> None:
        """
        Rotate the rectangle by the given angle.

        :param angle: The angle to rotate the rectangle by.
        """
        super().rotate_shape(angle, self.center, [self.top_left, self.top_right, self.bottom_left, self.bottom_right])

    def scale(self, factor: float) -> None:
        """
        Scale the rectangle by the given factor.

        :param factor: The factor to scale the rectangle by.
        """
        super().scale_shape(factor, self.center, [self.top_left, self.top_right, self.bottom_left, self.bottom_right])

    def update_center(self) -> None:
        """
        Update the center point of the rectangle.
        """
        self.center.set_point((self.top_left.x + self.top_right.x) / 2,
                              (self.top_left.y + self.bottom_left.y) / 2)

    def get_points_list(self) -> list[Point]:
        """
        Get a list of points defining the rectangle.

        :return: A list containing the four corner points of the rectangle.
        """
        return [self.top_left, self.top_right, self.bottom_left, self.bottom_right]

    def get_center(self) -> Point:
        """
        Get the center point of the rectangle.

        :return: The center point of the rectangle.
        """
        return self.center
