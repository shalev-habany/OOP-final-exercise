from abc import ABC, abstractmethod
from typing import List

import numpy as np
import cv2

from src.shapes.point import Point


class TransformShape(ABC):
    """
    An abstract base class for shapes that can be transformed.
    """

    def apply_operation_matrix(self, matrix: np.ndarray, points: List[Point]) -> None:
        """
        Apply a transformation matrix to a List of points.

        :param matrix: The transformation matrix.
        :param points: The List of points to transform.
        """
        for point in points:
            scaled_point = matrix @ np.array([[point.x], [point.y], [1]])
            point.set_point(scaled_point[0, 0], scaled_point[1, 0])

    def translate_shape(self, x_offset: float, y_offset: float, points: List[Point]) -> None:
        """
        Translate a shape by the given offsets.

        :param x_offset: The offset in the x direction.
        :param y_offset: The offset in the y direction.
        :param points: The List of points defining the shape.
        """
        for point in points:
            point.translate(x_offset, y_offset)
        self.update_center()

    def rotate_shape(self, angle: float, center: Point, points: List[Point]) -> None:
        """
        Rotate a shape by the given angle around its center.

        :param angle: The angle to rotate the shape by.
        :param center: The center point of the shape.
        :param points: The List of points defining the shape.
        """
        rotation_matrix = cv2.getRotationMatrix2D((center.x, center.y), angle, 1)
        self.apply_operation_matrix(rotation_matrix, points)

    def scale_shape(self, factor: float, center: Point, points: List[Point]) -> None:
        """
        Scale a shape by the given factor around its center.

        :param factor: The factor to scale the shape by.
        :param center: The center point of the shape.
        :param points: The List of points defining the shape.
        """
        scale_matrix = cv2.getRotationMatrix2D((center.x, center.y), 0, factor)
        self.apply_operation_matrix(scale_matrix, points)

    @abstractmethod
    def update_center(self):
        """
        Update the center point of the shape.
        """
        pass