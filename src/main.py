from src.canvas import Canvas
from src.json_parser.json_handler import JsonHandler
from src.shape_creators.shape_container import ShapeContainer
from src.shape_creators.shape_creator import ShapeCreator
from src.shape_creators.shape_factory import ShapeFactory
from src.shapes.shape import Shape

if __name__ == '__main__':
    canvas = Canvas(800, 800)
    json_path = 'inputs/shapes_example.json'
    json_handler = JsonHandler(json_path)
    shapes = json_handler.get_shapes()
    composite_shapes = json_handler.get_composite_shapes()
    shape_factory = ShapeFactory()
    shape_creator = ShapeCreator(canvas, shape_factory, json_handler.get_actions())
    shape_creator.create_shapes(shapes)
    shape_creator.create_composite_shapes(composite_shapes)
    canvas.draw()
    canvas.display()
