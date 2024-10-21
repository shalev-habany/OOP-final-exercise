from numpy import ndarray

from src.shapes.shape import Shape
import cv2


class Point(Shape):
    """
    A class representing a point shape.
    """

    def __init__(self, x: float, y: float, line_color: tuple[float, float, float]):
        """
        Initialize a Point instance.

        :param x: The x-coordinate of the point.
        :param y: The y-coordinate of the point.
        :param line_color: The color of the point.
        """
        self.x = x
        self.y = y
        self.line_color = line_color

    def draw(self, image: ndarray) -> ndarray:
        """
        Draw the point on the given image.

        :param image: The image on which to draw the point.
        :return: The image with the point drawn on it.
        """
        cv2.circle(image, (int(self.x), int(self.y)), 1, self.line_color, -1)
        return image

    def rotate(self, angle: float) -> None:
        """
        Rotate the point by the given angle. (No-op for points)

        :param angle: The angle to rotate the point by.
        """
        pass

    def translate(self, x_offset: float, y_offset: float) -> None:
        """
        Translate the point by the given offsets.

        :param x_offset: The offset in the x direction.
        :param y_offset: The offset in the y direction.
        """
        self.x += x_offset
        self.y += y_offset

    def scale(self, factor: float) -> None:
        """
        Scale the point by the given factor. (No-op for points)

        :param factor: The factor to scale the point by.
        """
        pass

    def set_point(self, x: float, y: float) -> None:
        """
        Set the coordinates of the point.

        :param x: The new x-coordinate of the point.
        :param y: The new y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def get_points_list(self) -> list['Point']:
        """
        Get a list of points defining the point.

        :return: A list containing the point itself.
        """
        return [self]

    def get_center(self) -> 'Point':
        """
        Get the center point of the point.

        :return: The point itself.
        """
        return self
