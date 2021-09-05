from typing import Any
import pytest

from main import validall_decorator, InputParameterVerificationError
from tests.constant_test_cases import VALID_INPUT_PARAMETER_VERIFICATION_ERROR_CASES
from tests.functions import function_one, function_two, function_for_default_behavior


@validall_decorator(input_validation=function_one,
                    result_validation=function_two, on_fail_repeat_times=1,
                    default_behavior=function_for_default_behavior)  # type: ignore
def my_function(input_variable: dict) -> str:
    print('Я декорируемая функция')
    return input_variable.__str__().upper()


@pytest.mark.parametrize('test_case', VALID_INPUT_PARAMETER_VERIFICATION_ERROR_CASES)  # type: ignore
def test_raise_exception(test_case: Any) -> None:
    with pytest.raises(InputParameterVerificationError):
        test_input = test_case.get("test_input")
        my_function(test_input)
