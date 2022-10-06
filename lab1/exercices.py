import math


def ex1() -> int:
    gcd = 0
    try:
        while val := int(input("number:")):
            gcd = math.gcd(gcd, val)
    except EOFError:
        pass
    return gcd


def ex2(string: str) -> int:
    return len([ch for ch in string if ch in "aeiouAEIOU"])


def ex3(str1: str, str2: str) -> int:
    return str2.count(str1)


def ex4(string: str) -> str:
    out = ""

    for index, ch in enumerate(string):
        if index == 0:
            out += ch.lower()
            continue
        if ch.isupper():
            out += f"_{ch.lower()}"
        else:
            out += ch

    return out


def ex5(matrix: list[list[str]], *, level: int = 0) -> str:
    lines, cols = len(matrix), len(matrix)
    out = ""

    if level >= lines // 2 and level >= cols // 2:
        return ""

    left, right, top, bottom = level, cols - 1 - level, level, lines - 1 - level
    for j in range(left, right):
        out += matrix[top][j]

    for i in range(top, bottom):
        out += matrix[i][right]

    for j in range(right, left, -1):
        out += matrix[bottom][j]

    for i in range(bottom, top, -1):
        out += matrix[i][left]

    out += ex5(matrix, level=level + 1)
    return out


def ex6(number: int) -> bool:
    num_str = str(abs(number))
    return num_str[: len(num_str) // 2] == num_str[: (len(num_str) - 1) // 2 : -1]


def ex7(string: str) -> int:
    first_occurrence = 0
    for index, ch in enumerate(string):
        if ch.isnumeric() and first_occurrence == 0:
            first_occurrence = index
        elif not ch.isnumeric() and first_occurrence != 0:
            return int(string[first_occurrence:index])

    raise Exception("Positive number not found")


def ex8(number: int) -> int:
    counter = 0

    while number:
        counter += number & 0x01
        number //= 2

    return counter


def ex9(string: str) -> tuple[int, str]:
    occurrences: dict[str, int] = {}

    for ch in string.replace(" ", ""):
        if not ch.lower() in occurrences:
            occurrences[ch.lower()] = 1
        else:
            occurrences[ch.lower()] += 1

    max_val = 0
    ch_found = ""
    for val in occurrences:
        if occurrences[val] > max_val:
            max_val = occurrences[val]
            ch_found = val

    return (max_val, ch_found)


def ex10(string: str) -> int:
    return len([ele for ele in string.split(" ") if len(ele) > 0])
