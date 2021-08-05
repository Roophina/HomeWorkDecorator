# публичные тестовые случаи из текста условия задачи
VALID_JSON_TEST_CASES = [
    {"test_input": {'city': 'Kazan'},
     "expected": "{'CITY': 'KAZAN'}"}]
VALID_STR_TEST_CASES = [
    {"test_input": {'city': 'Innopolis'},
     "expected": "{'CITY': 'INNOPOLIS'}"}]
VALID_INPUT_PARAMETER_VERIFICATION_ERROR_CASES = [
    {"test_input": {'country': 'London'},
     "expected": "InputParameterVerificationError"}]
VALID_RESULT_VERIFICATION_ERROR_CASES = [
    {"test_input": {'city': '1111'},
     "expected": "ResultVerificationError"}]
