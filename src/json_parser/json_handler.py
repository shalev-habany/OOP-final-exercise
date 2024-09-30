import json
from jsonschema import validate

from src.json_parser.json_schemas import SHAPES_SCHEMA, COMPOSITE_SHAPES_SCHEMA, ACTIONS_SCHEMA


class JsonHandler:
    def __init__(self, json_path):
        self.json_path = json_path
        self.json_data = self.read_json()

    def read_json(self):
        with open(self.json_path, 'r') as json_file:
            return json.load(json_file)

    def get_shapes(self):
        try:
            return self.json_data['shapes']
        except KeyError:
            return []

    def get_composite_shapes(self):
        try:
            return self.json_data['composite_shapes']
        except KeyError:
            return []

    def get_actions(self):
        try:
            return self.json_data['actions']
        except KeyError:
            return []

    def get_shape_by_id(self, shape_id):
        for shape in self.get_shapes():
            if shape['id'] == shape_id:
                return shape

    def get_composite_shape_by_id(self, composite_shape_id):
        for composite_shape in self.get_composite_shapes():
            if composite_shape['id'] == composite_shape_id:
                return composite_shape

    def get_actions_by_shape_id(self, action_id):
        shape_actions = []
        for action in self.get_actions():
            if action['shape_id'] == action_id:
                shape_actions.append(action)
        return shape_actions

    def validate_json(self):
        schema = {
            'type': 'object',
            'properties': {
                'shapes': SHAPES_SCHEMA,
                'composite_shapes': COMPOSITE_SHAPES_SCHEMA,
                'actions': ACTIONS_SCHEMA
            }
        }
        validate(self.json_data, schema)
