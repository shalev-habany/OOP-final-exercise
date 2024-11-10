import json
from typing import Dict, List

from jsonschema import validate

from src.json_parser.json_schemas import SHAPES_SCHEMA, COMPOSITE_SHAPES_SCHEMA, ACTIONS_SCHEMA


class JsonHandler:
    """
    Class to handle JSON file operations, including reading, parsing, and validating JSON data.
    """

    def __init__(self, json_path: str):
        """
        Initialize the JsonHandler with the path to the JSON file.

        :param json_path: Path to the JSON file.
        """
        self.json_path = json_path
        self.json_data = JsonHandler.read_json(json_path)

    @staticmethod
    def read_json(json_path: str) -> Dict:
        """
        Read the JSON file and return its content as a dictionary.

        :param json_path: Path to the JSON file.
        :return: Dictionary containing the JSON data.
        """
        with open(json_path, 'r') as json_file:
            return json.load(json_file)

    def get_shapes(self) -> List:
        """
        Retrieve the List of shapes from the JSON data.

        :return: List of shapes.
        """
        return self.json_data.get('shapes', [])

    def get_composite_shapes(self) -> List:
        """
        Retrieve the List of composite shapes from the JSON data.

        :return: List of composite shapes.
        """
        return self.json_data.get('composite_shapes', [])

    def get_actions(self) -> List:
        """
        Retrieve the List of actions from the JSON data.

        :return: List of actions.
        """
        return self.json_data.get('actions', [])


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
