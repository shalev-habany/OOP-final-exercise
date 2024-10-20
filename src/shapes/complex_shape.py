from numpy import ndarray

from src.shapes.point import Point
from src.shapes.shape import Shape
from src.transform_shapes.transform_shapes import TransformShape


class ComplexShape(Shape, TransformShape):
    def __init__(self, shapes: list, line_color: tuple[float, float, float], image: ndarray):
        self.shapes = shapes
        self.line_color = line_color
        self.image = image
        self.center = self.get_center()
        self.points_list = []
        self.get_shapes_points_list(self)

    # def get_shapes_points_list(self) -> list[Point]:
    #     points_list = []
    #     for shape in self.shapes:
    #         shape_points = shape.get_points_list()
    #         points_list = [*points_list, *shape_points]
    #     return points_list

    def get_shapes_points_list(self, complex_shape: 'ComplexShape'):
        if not complex_shape.__class__.__name__ == 'ComplexShape':
            shape_points = complex_shape.get_points_list()
            self.points_list = [*self.points_list, *shape_points]
            return
        for shape in complex_shape.shapes:
            self.get_shapes_points_list(shape)

    def get_points_list(self) -> list[Point]:
        pass

    def translate(self, x_offset: float, y_offset: float) -> None:
        for shape in self.shapes:
            shape.translate(x_offset, y_offset)
        self.center = self.get_center()
        self.get_shapes_points_list(self)

    def rotate(self, angle: float) -> None:
        super().rotate_shape(angle, self.center, self.points_list)

    def scale(self, factor: float) -> None:
        super().scale_shape(factor, self.center, self.points_list)

    def draw(self, image: ndarray) -> ndarray:
        for shape in self.shapes:
            shape.draw(image)
        return image

    def get_center(self) -> Point:
        x = 0
        y = 0
        for shape in self.shapes:
            center: Point = shape.get_center()
            x += center.x
            y += center.y
        return Point(x / len(self.shapes), y / len(self.shapes), self.line_color, self.image)

    def update_center(self) -> None:
        self.center = self.get_center()
