from abc import ABC, abstractmethod
from typing import List

import numpy as np
import cv2
from aiohttp.web_routedef import static

from src.shapes.point import Point
from src.shapes.shape import Shape


class TransformShape(ABC):
    """
    An abstract base class for shapes that can be transformed.
    """

    @staticmethod
    def apply_operation_matrix(matrix: np.ndarray, points: List[Point]) -> None:
        """
        Apply a transformation matrix to a List of points.

        :param matrix: The transformation matrix.
        :param points: The List of points to transform.
        """
        for point in points:
            scaled_point = matrix @ np.array([[point.x], [point.y], [1]])
            point.set_point(scaled_point[0, 0], scaled_point[1, 0])

    @staticmethod
    def translate_shape(shape: Shape, x_offset: float, y_offset: float, points: List[Point]) -> None:
        """
        Translate a shape by the given offsets.

        :param shape: The shape to translate.
        :param x_offset: The offset in the x direction.
        :param y_offset: The offset in the y direction.
        :param points: The List of points defining the shape.
        """
        for point in points:
            point.translate(x_offset, y_offset)
        shape.update_center()

    @staticmethod
    def rotate_shape(angle: float, center: Point, points: List[Point]) -> None:
        """
        Rotate a shape by the given angle around its center.

        :param angle: The angle to rotate the shape by.
        :param center: The center point of the shape.
        :param points: The List of points defining the shape.
        """
        rotation_matrix = cv2.getRotationMatrix2D((center.x, center.y), angle, 1)
        TransformShape.apply_operation_matrix(rotation_matrix, points)

    @staticmethod
    def scale_shape(factor: float, center: Point, points: List[Point]) -> None:
        """
        Scale a shape by the given factor around its center.

        :param factor: The factor to scale the shape by.
        :param center: The center point of the shape.
        :param points: The List of points defining the shape.
        """
        scale_matrix = cv2.getRotationMatrix2D((center.x, center.y), 0, factor)
        TransformShape.apply_operation_matrix(scale_matrix, points)