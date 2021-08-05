from main import validall_decorator
from tests.constant_test_cases import VALID_STR_TEST_CASES
from tests.functions import function_one, function_two, function_for_default_behavior


@validall_decorator(input_validation=function_one,
                    result_validation=function_two, on_fail_repeat_times=1,
                    default_behavior=function_for_default_behavior)
def my_function(input_variable: dict) -> str:
    print('Я декорируемая функция')
    return input_variable.__str__().upper()


def test_validall_decorator() -> None:
    for test_case in VALID_STR_TEST_CASES:
        test_input = test_case.get("test_input")
        expected = test_case.get("expected")
        actual = my_function(test_input)
        assert actual == expected
