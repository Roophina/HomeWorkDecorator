"""Декоратор."""
from typing import Any, Callable
from functools import wraps


class ResultVerificationError(Exception):
    """Исключение при провале проверки результата выполнения функции."""

    def __init__(self, *args: Any):
        """Переопределение метода конструктора."""
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """Переопределение магического метода для читаемости ошибки, выводимой на экран."""
        if self.message:
            return "ResultVerificationError, {0}".format(self.message)
        else:
            return "ResultVerificationError has been raised"


class InputParameterVerificationError(Exception):
    """Исключение при провале проверки входных параметров."""

    def __init__(self, *args: Any):
        """Переопределение метода конструктора."""
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self) -> str:
        """Переопределение магического метода для читаемости ошибки, выводимой на экран."""
        if self.message:
            return "InputParameterVerificationError, {0}".format(self.message)
        else:
            return "InputParameterVerificationError has been raised"


class MyException(Exception):
    """Исключение при установке параметра on_fail_repeat_times в 0."""

    def __init__(self) -> None:
        """Переопределение метода конструктора."""
        self.message = None

    def __str__(self) -> str:
        """Переопределение магического метода для читаемости ошибки, выводимой на экран."""
        return "Параметр on_fail_repeat_times равен 0"


def validall_decorator(
    input_validation: Callable,
    result_validation: Callable,
    on_fail_repeat_times: int = 1,
    default_behavior: Callable = None,
) -> Callable:
    """Декоратор с параметрами."""

    def decoration(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not input_validation(*args, **kwargs):
                raise InputParameterVerificationError
            print("то что происходит ДО вызова функции")
            if on_fail_repeat_times == 0:
                raise MyException
            counter = on_fail_repeat_times
            while counter != 0:
                result = function(*args, **kwargs)
                res = result_validation(result)
                if res:
                    break
                counter -= 1
            if not res:
                if default_behavior:
                    print("вызывается дефолтная функция")
                    default_behavior()
                else:
                    raise ResultVerificationError
            print("то что происходит ПОСЛЕ вызова функции")
            return result

        return wrapper

    return decoration
