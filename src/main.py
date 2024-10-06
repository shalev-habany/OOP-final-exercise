from src.canvas import Canvas
from src.json_parser.json_handler import JsonHandler
from src.shape_creators.shape_container import ShapeContainer
from src.shape_creators.shape_factory import ShapeFactory

if __name__ == '__main__':
    canvas = Canvas(800, 800)
    json_path = 'inputs/shapes_example.json'
    json_handler = JsonHandler(json_path)
    shapes = json_handler.get_shapes()
    composite_shapes = json_handler.get_composite_shapes()
    shape_factory = ShapeFactory(canvas.image)
    shapes_instances = []
    for shape in shapes:
        shape_instance = shape_factory.create_shape(shape['type'], shape['line_color'], shape['shape_props'])
        shape_actions = json_handler.get_actions_by_shape_id(shape['id'])
        shape_container = ShapeContainer.create_final_shape_for_canvas(shape['id'], shape_instance, shape_actions)
        canvas.add_shape(shape_container.get_shape())
    for composite_shape in composite_shapes:
        composite_shape_instance = shape_factory.create_shape(composite_shape['type'], composite_shape['line_color'], composite_shape)
        composite_shape_actions = json_handler.get_actions_by_shape_id(composite_shape['id'])
        composite_shape_container = ShapeContainer.create_final_shape_for_canvas(composite_shape['id'], composite_shape_instance, composite_shape_actions)
        canvas.add_shape(composite_shape_container.get_shape())
    canvas.draw()
    canvas.display()
