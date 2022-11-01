import sympy
from typing import Callable


def process_item(x: int) -> int:
    prime = sympy.nextprime(x)
    if prime is None:
        raise ValueError("sympy.nextprime returned None")
    return int(prime)


ex2_anon_func = lambda *args, **kwargs: sum(kwargs.values())


def ex2_named_func(*args: int | float, **kwargs: int | float) -> int | float:
    return sum(kwargs.values())


def ex3(value: str) -> list[str]:
    return list(val for val in filter(lambda x: x.lower() in "aeiou", value))


def __has_string_key(d: dict, char_min: int) -> bool:
    for item in d:
        if isinstance(item, str) and len(item) >= char_min:
            return True

    return False


def ex4(*args, **kwargs) -> list[dict]:
    out: list[dict] = []

    for item in args + tuple(kwargs.values()):
        if isinstance(item, dict) and len(item) >= 2 and __has_string_key(item, 3):
            out.append(item)

    return out


def ex5(lst: list) -> list[int | float]:
    return list(filter(lambda x: isinstance(x, (int, float)), lst))


def ex6(lst: list[int]) -> list[tuple[int, int]]:
    return list(
        zip(filter(lambda x: x % 2 == 0, lst), filter(lambda x: x % 2 == 1, lst))
    )


def __passes_all_predicates(val: int, predicates: list[Callable[[int], bool]]) -> bool:
    for pred in predicates:
        if not pred(val):
            return False

    return True


def ex7(**kwargs) -> list[int]:
    HARD_LIMIT = 1000
    filters: list[Callable[[int], bool]] = []
    limit = 1000
    offset = 0

    if "filters" in kwargs:
        filters = kwargs["filters"]
        for filter in filters:
            if not isinstance(filter, Callable):
                raise ValueError("Filters must be predicates (int) -> bool")
    if "limit" in kwargs:
        try:
            limit = int(kwargs["limit"])
        except ValueError:
            raise ValueError("Limit parameter must be an int")
    if "offset" in kwargs:
        try:
            offset = kwargs["offset"]
        except ValueError:
            raise ValueError("Offset parameter must be an int")

    if limit > HARD_LIMIT:
        raise ValueError(
            f"Input value {limit} exceeds possible generated values {HARD_LIMIT}"
        )
    if offset > limit or offset > HARD_LIMIT or offset < 0:
        raise ValueError(f"Offset value should be 0 <= offset < {limit}")

    out: list[int] = []
    a = 0
    b = 1
    added = index = 0
    while added < limit:
        if not __passes_all_predicates(a, filters):
            a, b = b, a + b
            continue

        if index >= offset:
            out.append(a)
            added += 1

        a, b = b, a + b
        index += 1
    return out


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


# def ex8(func:Callable) -> None:
#     print(f"Arguments are {args} and will return -")


def ex9(pairs: list[tuple[int, int]]) -> list[dict[str, int | float]]:
    return [
        {"sum": pair[0] + pair[1], "prod": pair[0] * pair[1], "pow": pair[0] ** pair[1]}
        for pair in pairs
    ]
