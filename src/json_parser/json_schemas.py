SHAPES_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'id': {'type': 'string'},
            'type': {
                'type': 'string',
                'enum': ['circle', 'rectangle', 'triangle', 'line', 'point']
            },
            'shape_props': {'type': 'object'},
            'line_color': {'type': 'array', 'items': {'type': 'number'}}
        }
    }
}
COMPOSITE_SHAPES_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'id': {'type': 'string'},
            'type': {'type': 'string'},
            'shapes': SHAPES_SCHEMA,
            'line_color': {'type': 'array', 'items': {'type': 'number'}}
        }
    }
}
ACTIONS_SCHEMA = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'shape_id': {'type': 'string'},
            'type': {
                'type': 'string',
                'enum': ['rotate', 'scale', 'translate']
            },
            'angle': {'type': 'number'},
            'factor': {'type': 'number'},
            'x_offset': {'type': 'number'},
            'y_offset': {'type': 'number'}
        }
    }
}
