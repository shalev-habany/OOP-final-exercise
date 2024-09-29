from abc import ABC, abstractmethod

import numpy as np
import cv2

from src.shapes.point import Point


class TransformShape(ABC):
    def apply_operation_matrix(self, matrix: np.ndarray, points: list[Point]) -> None:
        for point in points:
            scaled_point = matrix @ np.array([[point.x], [point.y], [1]])
            point.set_point(scaled_point[0, 0], scaled_point[1, 0])

    def translate_shape(self, x_offset: float, y_offset: float, points: list[Point]) -> None:
        for point in points:
            point.translate(x_offset, y_offset)
        self.update_center()

    def rotate_shape(self, angle: float, center: Point, points: list[Point]) -> None:
        rotation_matrix = cv2.getRotationMatrix2D((center.x, center.y), angle, 1)
        self.apply_operation_matrix(rotation_matrix, points)

    def scale_shape(self, factor: float, center: Point, points: list[Point]) -> None:
        scale_matrix = cv2.getRotationMatrix2D((center.x, center.y), 0, factor)
        self.apply_operation_matrix(scale_matrix, points)

    @abstractmethod
    def update_center(self):
        pass
