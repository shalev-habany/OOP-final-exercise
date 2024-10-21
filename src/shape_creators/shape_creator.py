from copy import deepcopy

from src.canvas import Canvas
from src.shape_creators.shape_container import ShapeContainer
from src.shape_creators.shape_factory import ShapeFactory
from src.shapes.composite_shape import CompositeShape


class ShapeCreator:
    """
    A class responsible for creating shapes and composite shapes on a canvas.
    """

    def __init__(self, canvas: Canvas, shape_factory: ShapeFactory, actions: list):
        """
        Initialize the ShapeCreator with a canvas, shape factory, and a list of actions.

        :param canvas: The canvas where shapes will be drawn.
        :param shape_factory: A factory to create shape instances.
        :param actions: A list of actions to be applied to shapes.
        """
        self.canvas = canvas
        self.shape_factory = shape_factory
        self.actions = actions
        self.created_shapes: list[ShapeContainer] = []

    def get_actions_by_shape_id(self, shape_id: str):
        """
        Retrieve actions associated with a specific shape ID.

        :param shape_id: The ID of the shape to retrieve actions for.
        :return: A list of actions associated with the shape ID.
        """
        shape_actions = []
        for action in self.actions:
            if action['shape_id'] == shape_id:
                shape_actions.append(action)
        return shape_actions

    def create_shapes(self, shapes: list):
        """
        Create and add shapes to the canvas.

        :param shapes: A list of shape dictionaries to be created.
        """
        for shape in shapes:
            shape_instance = self.shape_factory.create_shape(shape['type'], shape['line_color'], shape['shape_props'])
            shape_actions = self.get_actions_by_shape_id(shape['id'])
            shape_container = ShapeContainer.create_final_shape_for_canvas(shape['id'], shape_instance, shape_actions,
                                                                           shape['type'])
            self.canvas.add_shape(shape_container.get_shape())
            self.created_shapes.append(shape_container)

    def create_composite_shape(self, composite_shape: dict):
        """
        Create and add a composite shape to the canvas.

        :param composite_shape: A dictionary representing the composite shape to be created.
        """
        composite_shape_instance = self.shape_factory.create_shape(composite_shape['type'],
                                                                   composite_shape['line_color'], composite_shape)
        composite_shape_actions = self.get_actions_by_shape_id(composite_shape['id'])
        composite_shape_container = ShapeContainer.create_final_shape_for_canvas(composite_shape['id'],
                                                                                 composite_shape_instance,
                                                                                 composite_shape_actions,
                                                                                 composite_shape['type'],
                                                                                 composite_shape['draw'])
        self.created_shapes.append(composite_shape_container)
        if composite_shape['draw']:
            self.canvas.add_shape(composite_shape_container.get_shape())

    def create_nested_composite_shape(self, composite_shape: dict):
        """
        Create and add a nested composite shape to the canvas.

        :param composite_shape: A dictionary representing the nested composite shape to be created.
        """
        shape_containers = []
        for shape in composite_shape['shapes']:
            shape_type = shape['type']
            for created_shape in self.created_shapes:
                if created_shape.type == shape_type:
                    shape_actions = self.get_actions_by_shape_id(shape['id'])
                    shape_containers.append(
                        ShapeContainer.create_final_shape_for_canvas(shape["id"], deepcopy(created_shape.get_shape()),
                                                                     shape_actions, shape["type"]))
                    break
        shapes_list = [shape_container.get_shape() for shape_container in shape_containers]
        composite_shape_instance = CompositeShape(shapes_list, composite_shape['line_color'])
        composite_shape_actions = self.get_actions_by_shape_id(composite_shape['id'])
        composite_shape_container = ShapeContainer.create_final_shape_for_canvas(composite_shape['id'],
                                                                                 composite_shape_instance,
                                                                                 composite_shape_actions,
                                                                                 composite_shape['type'],
                                                                                 composite_shape['draw'])
        self.created_shapes.append(composite_shape_container)
        if composite_shape['draw']:
            self.canvas.add_shape(composite_shape_container.get_shape())

    def create_composite_shapes(self, composite_shapes: list):
        """
        Create and add multiple composite shapes to the canvas.

        :param composite_shapes: A list of composite shape dictionaries to be created.
        """
        for composite_shape in composite_shapes:
            if composite_shape['shapes'][0]['type'] in ['circle', 'rectangle', 'triangle', 'line', 'point']:
                self.create_composite_shape(composite_shape)
            else:
                self.create_nested_composite_shape(composite_shape)
