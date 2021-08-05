import sys
import os
import jsonschema
import re
from main import validall_decorator
from tests.constant_test_cases import VALID_JSON_TEST_CASES

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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


@validall_decorator(input_validation=function_one,
                    result_validation=function_two, on_fail_repeat_times=1,
                    default_behavior=function_for_default_behavior)
def my_function(input_variable: dict) -> str:
    print('Я декорируемая функция')
    return input_variable.__str__().upper()


def test_validall_decorator() -> None:
    for test_case in VALID_JSON_TEST_CASES:
        test_input = test_case.get("test_input")
        expected = test_case.get("expected")
        actual = my_function(test_input)
        assert actual == expected
