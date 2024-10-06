from src.shapes.circle import Circle
from src.shapes.complex_shape import ComplexShape
from src.shapes.line import Line
from src.shapes.point import Point
from src.shapes.rectangle import Rectangle
from src.shapes.shape import Shape
from src.shapes.triangle import Triangle


class ShapeFactory:

    def __init__(self, image):
        self.image = image

    def create_shape(self, shape_type: str, line_color: tuple[float, float, float], shape_props: dict) -> Shape:
        if shape_type == 'circle':
            return self.create_circle(line_color, shape_props)
        elif shape_type == 'rectangle':
            return self.create_rectangle(line_color, shape_props)
        elif shape_type == 'triangle':
            return self.create_triangle(line_color, shape_props)
        elif shape_type == 'line':
            return self.create_line(line_color, shape_props)
        elif shape_type == 'point':
            return self.create_point(line_color, shape_props)
        else:
            return self.create_composite_shape(line_color, shape_props)

    def create_point(self, line_color: tuple[float, float, float], shape_props: dict) -> Shape:
        return Point(shape_props['x'], shape_props['y'], line_color, self.image)

    def create_circle(self, line_color: tuple[float, float, float], shape_props: dict) -> Shape:
        shape_props['center'] = Point(shape_props['center']['x'], shape_props['center']['y'], line_color, self.image)
        return Circle(shape_props['radius'], shape_props['center'], line_color, self.image)

    def create_rectangle(self, line_color: tuple[float, float, float], shape_props: dict) -> Shape:
        shape_props['center'] = Point(shape_props['center']['x'], shape_props['center']['y'], line_color, self.image)
        return Rectangle(shape_props['center'], shape_props['width'], shape_props['height'], line_color, self.image)

    def create_triangle(self, line_color: tuple[float, float, float], shape_props: dict) -> Shape:
        shape_props['point1'] = Point(shape_props['point1']['x'], shape_props['point1']['y'], line_color, self.image)
        shape_props['point2'] = Point(shape_props['point2']['x'], shape_props['point2']['y'], line_color, self.image)
        shape_props['point3'] = Point(shape_props['point3']['x'], shape_props['point3']['y'], line_color, self.image)
        return Triangle(shape_props['point1'], shape_props['point2'], shape_props['point3'], line_color, self.image)

    def create_line(self, line_color: tuple[float, float, float], shape_props: dict) -> Shape:
        shape_props['point1'] = Point(shape_props['point1']['x'], shape_props['point1']['y'], line_color, self.image)
        shape_props['point2'] = Point(shape_props['point2']['x'], shape_props['point2']['y'], line_color, self.image)
        return Line(shape_props['point1'], shape_props['point2'], line_color, self.image)


    def create_composite_shape(self, line_color: tuple[float, float, float], shapes: dict) -> Shape:
        shapes_instances = []
        for shape in shapes['shapes']:
            shapes_instances.append(self.create_shape(shape['type'], line_color, shape['shape_props']))
        return ComplexShape(shapes_instances, line_color, self.image)