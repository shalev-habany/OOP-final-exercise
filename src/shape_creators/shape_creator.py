from copy import deepcopy

from src.canvas import Canvas
from src.shape_creators.shape_container import ShapeContainer
from src.shape_creators.shape_factory import ShapeFactory
from src.shapes.complex_shape import ComplexShape


class ShapeCreator:
    def __init__(self, canvas: Canvas, shape_factory: ShapeFactory, actions: list):
        self.canvas = canvas
        self.shape_factory = shape_factory
        self.actions = actions
        self.created_shapes: list[ShapeContainer] = []

    def get_actions_by_shape_id(self, shape_id: str):
        shape_actions = []
        for action in self.actions:
            if action['shape_id'] == shape_id:
                shape_actions.append(action)
        return shape_actions

    def create_shapes(self, shapes: list):
        for shape in shapes:
            shape_instance = self.shape_factory.create_shape(shape['type'], shape['line_color'], shape['shape_props'])
            shape_actions = self.get_actions_by_shape_id(shape['id'])
            shape_container = ShapeContainer.create_final_shape_for_canvas(shape['id'], shape_instance, shape_actions,
                                                                           shape['type'])
            self.canvas.add_shape(shape_container.get_shape())
            self.created_shapes.append(shape_container)

    def create_composite_shape(self, composite_shape: dict):
        composite_shape_instance = self.shape_factory.create_shape(composite_shape['type'],
                                                                   composite_shape['line_color'], composite_shape)
        composite_shape_actions = self.get_actions_by_shape_id(composite_shape['id'])
        composite_shape_container = ShapeContainer.create_final_shape_for_canvas(composite_shape['id'],
                                                                                 composite_shape_instance,
                                                                                 composite_shape_actions,
                                                                                 composite_shape['type'])
        self.canvas.add_shape(composite_shape_container.get_shape())
        self.created_shapes.append(composite_shape_container)

    def create_nested_composite_shape(self, composite_shape: dict):
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
        composite_shape_instance = ComplexShape(shapes_list,
                                                composite_shape['line_color'], self.canvas.image)
        composite_shape_actions = self.get_actions_by_shape_id(composite_shape['id'])
        composite_shape_container = ShapeContainer.create_final_shape_for_canvas(composite_shape['id'],
                                                                                 composite_shape_instance,
                                                                                 composite_shape_actions,
                                                                                 composite_shape['type'])
        self.canvas.add_shape(composite_shape_container.get_shape())
        self.created_shapes.append(composite_shape_container)

    def create_composite_shapes(self, composite_shapes: list):
        for composite_shape in composite_shapes:
            if composite_shape['shapes'][0]['type'] in ['circle', 'rectangle', 'triangle', 'line', 'point']:
                self.create_composite_shape(composite_shape)
            else:
                self.create_nested_composite_shape(composite_shape)
