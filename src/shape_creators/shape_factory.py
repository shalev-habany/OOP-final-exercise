from typing import Dict, Tuple

from src.shapes.circle import Circle
from src.shapes.composite_shape import CompositeShape
from src.shapes.line import Line
from src.shapes.point import Point
from src.shapes.rectangle import Rectangle
from src.shapes.shape import Shape
from src.shapes.triangle import Triangle


class ShapeFactory:
    """
        A factory class for creating various shapes.
    """
    
    def create_shape(self, shape_type: str, line_color: Tuple[float, float, float], shape_props: Dict) -> Shape:
        """
        Create a shape based on the specified type.

        :param shape_type: The type of the shape to create.
        :param line_color: The color of the shape's line.
        :param shape_props: The properties of the shape.
        :return: An instance of the created shape.
        """
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

    def create_point(self, line_color: Tuple[float, float, float], shape_props: Dict) -> Shape:
        """
        Create a point shape.

        :param line_color: The color of the point's line.
        :param shape_props: The properties of the point.
        :return: An instance of the Point shape.
        """
        return Point(shape_props['x'], shape_props['y'], line_color)

    def create_circle(self, line_color: Tuple[float, float, float], shape_props: Dict) -> Shape:
        """
        Create a circle shape.

        :param line_color: The color of the circle's line.
        :param shape_props: The properties of the circle.
        :return: An instance of the Circle shape.
        """
        shape_props['center'] = Point(shape_props['center']['x'], shape_props['center']['y'], line_color)
        return Circle(shape_props['radius'], shape_props['center'], line_color)

    def create_rectangle(self, line_color: Tuple[float, float, float], shape_props: Dict) -> Shape:
        """
        Create a rectangle shape.

        :param line_color: The color of the rectangle's line.
        :param shape_props: The properties of the rectangle.
        :return: An instance of the Rectangle shape.
        """
        shape_props['center'] = Point(shape_props['center']['x'], shape_props['center']['y'], line_color)
        return Rectangle(shape_props['center'], shape_props['width'], shape_props['height'], line_color)

    def create_triangle(self, line_color: Tuple[float, float, float], shape_props: Dict) -> Shape:
        """
        Create a triangle shape.

        :param line_color: The color of the triangle's line.
        :param shape_props: The properties of the triangle.
        :return: An instance of the Triangle shape.
        """
        shape_props['point1'] = Point(shape_props['point1']['x'], shape_props['point1']['y'], line_color)
        shape_props['point2'] = Point(shape_props['point2']['x'], shape_props['point2']['y'], line_color)
        shape_props['point3'] = Point(shape_props['point3']['x'], shape_props['point3']['y'], line_color)
        return Triangle(shape_props['point1'], shape_props['point2'], shape_props['point3'], line_color)

    def create_line(self, line_color: Tuple[float, float, float], shape_props: Dict) -> Shape:
        """
        Create a line shape.

        :param line_color: The color of the line's line.
        :param shape_props: The properties of the line.
        :return: An instance of the Line shape.
        """
        shape_props['point1'] = Point(shape_props['point1']['x'], shape_props['point1']['y'], line_color)
        shape_props['point2'] = Point(shape_props['point2']['x'], shape_props['point2']['y'], line_color)
        return Line(shape_props['point1'], shape_props['point2'], line_color)

    def create_composite_shape(self, line_color: Tuple[float, float, float], shapes: Dict) -> Shape:
        """
        Create a composite shape.

        :param line_color: The color of the composite shape's line.
        :param shapes: The properties of the composite shape.
        :return: An instance of the ComplexShape.
        """
        shapes_instances = []
        for shape in shapes['shapes']:
            shapes_instances.append(self.create_shape(shape['type'], line_color, shape['shape_props']))
        return CompositeShape(shapes_instances, line_color)