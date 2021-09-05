import re

import jsonschema


def function_one(dict_json: dict) -> bool:
    my_schema = {
        "type": "object",
        "required": [
            "city"
        ],
        "additionalProperties": False,
        "properties": {
            "city": {
                "type": "string"
            }
        }
    }

    try:
        jsonschema.validate(instance=dict_json, schema=my_schema)
    except jsonschema.ValidationError:
        return False
    return True


def function_two(a: str) -> bool:
    pattern = re.compile(r'{\D*}')
    return bool(pattern.match(a))


def function_for_default_behavior() -> bool:
    print('Я функция по умолчанию')
    return True
