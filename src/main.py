from src.canvas import Canvas
from src.json_parser.json_handler import JsonHandler
from src.shape_creators.shape_container import ShapeContainer
from src.shape_creators.shape_factory import ShapeFactory

if __name__ == '__main__':
    canvas = Canvas(800, 800)
    json_path = './inputs/basic_shapes.json'
    json_handler = JsonHandler(json_path)
    shapes = json_handler.get_shapes()
    shape_factory = ShapeFactory(canvas.image)
    shapes_instances = []
    for shape in shapes:
        shape_instance = shape_factory.create_shape(shape['type'], shape['line_color'], shape['shape_props'])
        shape_actions = json_handler.get_actions_by_shape_id(shape['id'])
        shape_container = ShapeContainer.create_final_shape_for_canvas(shape['id'], shape_instance, shape_actions)
        canvas.add_shape(shape_container.get_shape())
    canvas.draw()
    canvas.display()
