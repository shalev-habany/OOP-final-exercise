from typing import List, Tuple

from numpy import ndarray

from src.shapes.point import Point
from src.shapes.shape import Shape
from src.transform_shapes.transform_shapes import TransformShape


class CompositeShape(Shape, TransformShape):
    """
    A class representing a composite shape, which is a collection of multiple shapes.
    """

    def __init__(self, shapes: List, line_color: Tuple[float, float, float]):
        """
        Initialize a CompositeShape instance.

        :param shapes: A list of shapes that make up the composite shape.
        :param line_color: The color of the composite shape's line.
        """
        self.shapes = shapes
        self.line_color = line_color
        self.center = self.get_center()
        self.points_list = []
        self.set_shapes_points_list(self)

    def set_shapes_points_list(self, composite_shape: 'CompositeShape') -> None:
        """
        Set the points list for the composite shape.

        :param composite_shape: The composite shape instance.
        """
        if not composite_shape.__class__.__name__ == 'CompositeShape':
            shape_points = composite_shape.get_points_list()
            self.points_list = [*self.points_list, *shape_points]
            return
        for shape in composite_shape.shapes:
            self.set_shapes_points_list(shape)

    def get_points_list(self) -> List[Point]:
        """
        Get a list of points defining the composite shape.

        :return: A list of points.
        """
        pass

    def translate(self, x_offset: float, y_offset: float) -> None:
        """
        Translate the composite shape by the given offsets.

        :param x_offset: The offset in the x direction.
        :param y_offset: The offset in the y direction.
        """
        for shape in self.shapes:
            shape.translate(x_offset, y_offset)
        self.center = self.get_center()
        self.set_shapes_points_list(self)

    def rotate(self, angle: float) -> None:
        """
        Rotate the composite shape by the given angle.

        :param angle: The angle to rotate the composite shape by.
        """
        super().rotate_shape(angle, self.center, self.points_list)

    def scale(self, factor: float) -> None:
        """
        Scale the composite shape by the given factor.

        :param factor: The factor to scale the composite shape by.
        """
        super().scale_shape(factor, self.center, self.points_list)

    def draw(self, image: ndarray) -> ndarray:
        """
        Draw the composite shape on the given image.

        :param image: The image on which to draw the composite shape.
        :return: The image with the composite shape drawn on it.
        """
        for shape in self.shapes:
            shape.draw(image)
        return image

    def get_center(self) -> Point:
        """
        Get the center point of the composite shape.

        :return: The center point of the composite shape.
        """
        x = 0
        y = 0
        for shape in self.shapes:
            center: Point = shape.get_center()
            x += center.x
            y += center.y
        return Point(x / len(self.shapes), y / len(self.shapes), self.line_color)

    def update_center(self) -> None:
        """
        Update the center point of the composite shape.
        """
        self.center = self.get_center()