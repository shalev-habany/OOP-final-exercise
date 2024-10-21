import json
from jsonschema import validate

from src.json_parser.json_schemas import SHAPES_SCHEMA, COMPOSITE_SHAPES_SCHEMA, ACTIONS_SCHEMA


class JsonHandler:
    """
    Class to handle JSON file operations, including reading, parsing, and validating JSON data.
    """

    def __init__(self, json_path):
        """
        Initialize the JsonHandler with the path to the JSON file.

        :param json_path: Path to the JSON file.
        """
        self.json_path = json_path
        self.json_data = self.read_json()

    def read_json(self) -> dict:
        """
        Read the JSON file and return its content as a dictionary.

        :return: Dictionary containing the JSON data.
        """
        with open(self.json_path, 'r') as json_file:
            return json.load(json_file)

    def get_shapes(self) -> list:
        """
        Retrieve the list of shapes from the JSON data.

        :return: List of shapes.
        """
        try:
            return self.json_data['shapes']
        except KeyError:
            return []

    def get_composite_shapes(self) -> list:
        """
        Retrieve the list of composite shapes from the JSON data.

        :return: List of composite shapes.
        """
        try:
            return self.json_data['composite_shapes']
        except KeyError:
            return []

    def get_actions(self) -> list:
        """
        Retrieve the list of actions from the JSON data.

        :return: List of actions.
        """
        try:
            return self.json_data['actions']
        except KeyError:
            return []

    def get_shape_by_id(self, shape_id) -> dict:
        """
        Retrieve a shape by its ID from the JSON data.

        :param shape_id: ID of the shape to retrieve.
        :return: Dictionary representing the shape.
        """
        for shape in self.get_shapes():
            if shape['id'] == shape_id:
                return shape

    def get_composite_shape_by_id(self, composite_shape_id) -> dict:
        """
        Retrieve a composite shape by its ID from the JSON data.

        :param composite_shape_id: ID of the composite shape to retrieve.
        :return: Dictionary representing the composite shape.
        """
        for composite_shape in self.get_composite_shapes():
            if composite_shape['id'] == composite_shape_id:
                return composite_shape

    def get_actions_by_shape_id(self, action_id) -> list:
        """
        Retrieve actions associated with a specific shape ID from the JSON data.

        :param action_id: ID of the shape to retrieve actions for.
        :return: List of actions associated with the shape ID.
        """
        shape_actions = []
        for action in self.get_actions():
            if action['shape_id'] == action_id:
                shape_actions.append(action)
        return shape_actions

    def validate_json(self) -> None:
        """
        Validate the JSON data against predefined schemas.

        :raises jsonschema.exceptions.ValidationError: If the JSON data does not conform to the schema.
        """
        schema = {
            'type': 'object',
            'properties': {
                'shapes': SHAPES_SCHEMA,
                'composite_shapes': COMPOSITE_SHAPES_SCHEMA,
                'actions': ACTIONS_SCHEMA
            }
        }
        validate(self.json_data, schema)
