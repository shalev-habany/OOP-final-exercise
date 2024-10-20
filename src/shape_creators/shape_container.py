from src.shapes.shape import Shape


class ShapeContainer:
    def __init__(self, shape_id: str, shape: Shape, actions: list[dict]):
        self.id = shape_id
        self.shape = shape
        self.actions = actions

    def get_shape(self) -> Shape:
        return self.shape

    def apply_actions(self) -> None:
        for action in self.actions:
            if action['type'] == 'rotate':
                self.shape.rotate(action['angle'])
            elif action['type'] == 'scale':
                self.shape.scale(action['factor'])
            elif action['type'] == 'translate':
                self.shape.translate(action['x_offset'], action['y_offset'])

    @staticmethod
    def create_final_shape_for_canvas(shape_id: str, shape: Shape, actions: list[dict]) -> 'ShapeContainer':
        shape_container = ShapeContainer(shape_id, shape, actions)
        shape_container.apply_actions()
        return shape_container
