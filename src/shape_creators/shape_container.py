from src.shapes.shape import Shape


class ShapeContainer:
    """
    A wrapper class for shapes, including their actions and type.
    """

    def __init__(self, shape_id: str, shape: Shape, actions: list[dict], type: str, draw: bool = True):
        """
        Initialize the ShapeContainer with a shape ID, shape instance, actions, and type.

        :param shape_id: The ID of the shape.
        :param shape: The shape instance.
        :param actions: A list of actions to be applied to the shape.
        :param type: The type of the shape.
        :param draw: A boolean indicating whether the shape should be drawn.
        """
        self.draw = draw
        self.id = shape_id
        self.shape = shape
        self.actions = actions
        self.type = type

    def get_shape(self) -> Shape:
        """
        Retrieve the shape instance.

        :return: The shape instance.
        """
        return self.shape

    def apply_actions(self) -> None:
        """
        Apply the actions to the shape.
        """
        for action in self.actions:
            if action['type'] == 'rotate':
                self.shape.rotate(action['angle'])
            elif action['type'] == 'scale':
                self.shape.scale(action['factor'])
            elif action['type'] == 'translate':
                self.shape.translate(action['x_offset'], action['y_offset'])

    @staticmethod
    def create_final_shape_for_canvas(shape_id: str, shape: Shape, actions: list[dict], type: str, draw: bool = True) -> 'ShapeContainer':
        """
        Create a ShapeContainer, apply actions to the shape, and return the container.

        :param shape_id: The ID of the shape.
        :param shape: The shape instance.
        :param actions: A list of actions to be applied to the shape.
        :param type: The type of the shape.
        :param draw: A boolean indicating whether the shape should be drawn.
        :return: A ShapeContainer instance with the actions applied.
        """
        shape_container = ShapeContainer(shape_id, shape, actions, type, draw)
        shape_container.apply_actions()
        return shape_container