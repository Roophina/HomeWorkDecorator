import sys
import os
from typing import Any

import jsonschema
import re

import pytest

from main import validall_decorator, ResultVerificationError
from tests.constant_test_cases import VALID_RESULT_VERIFICATION_ERROR_CASES

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


@validall_decorator(input_validation=function_one,
                    result_validation=function_two, on_fail_repeat_times=1,
                    default_behavior=None)
def my_function(input_variable: dict) -> str:
    print('Я декорируемая функция')
    return input_variable.__str__().upper()


@pytest.mark.parametrize('test_case', VALID_RESULT_VERIFICATION_ERROR_CASES)
def test_raise_exception(test_case: Any) -> None:
    with pytest.raises(ResultVerificationError):
        test_input = test_case.get("test_input")
        my_function(test_input)
