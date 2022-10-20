from typing import Any, TypeVar
import sympy


def ex1(n: int) -> list[int]:
    a = 0
    b = 1
    out: list[int] = []
    for _ in range(n):
        out.append(a)
        a, b = b, a + b

    return out


def ex2(number: list[int]) -> list[int]:
    return list(filter(lambda x: sympy.isprime(x), number))


T = TypeVar("T")


def ex3(a: list[T], b: list[T]) -> tuple[list[T], list[T], list[T], list[T]]:
    set_a = set(a)
    set_b = set(b)
    return (
        list(set_a.intersection(set_b)),
        list(set_a.union(set_b)),
        list(set_a - set_b),
        list(set_b - set_a),
    )


def ex4(notes: list[str], moves: list[int], start: int) -> list[str]:
    out: list[str] = []

    index = start
    for move in moves:
        out.append(notes[index])
        index += move
        index %= len(notes)
    out.append(notes[index])

    return out


def ex5(matrix: list[list[T]]) -> list[list[T]]:
    out: list[list[T]] = []
    for i in range(len(matrix)):
        out.append([])
        for j in range(len(matrix[0])):
            if i > j:
                out[i].append(0)  # type: ignore
            else:
                out[i].append(matrix[i][j])

    return out


def ex6(*lists: list, x: Any) -> list:
    current_freq: dict[int, int] = {}
    for lst in lists:
        for item in lst:
            try:
                current_freq[item] += 1
            except KeyError:
                current_freq[item] = 1

    return [item for item in current_freq if current_freq[item] == x]


def __is_palindrome(num: int) -> bool:
    return str(num) == (str(num))[::-1]


def ex7(numbers: list[int]) -> tuple[int, int]:
    palindromes = 0
    greatest_palindrome = -1

    for num in numbers:
        if __is_palindrome(num):
            palindromes += 1
            greatest_palindrome = max(greatest_palindrome, num)

    return (palindromes, greatest_palindrome)


def ex8(strings: list[str], x: int = 1, flag: bool = True) -> list[list[str]]:
    out: list[list[str]] = []

    for st in strings:
        current_list: list[str] = []
        for ch in st:
            if not not (ord(ch) % x) != flag:
                current_list.append(ch)
        out.append(current_list)

    return out


def ex9(matrix: list[list[int]]) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []

    for i in range(len(matrix) - 1, 0 - 1, -1):
        for j in range(len(matrix[0])):
            for k in range(0, i):
                if matrix[i][j] < matrix[k][j]:
                    out.append((i, j))
                    break

    return out


def ex10(*lists: list) -> list[tuple]:
    # return list(zip(*lists))
    max_len = max(len(lst) for lst in lists)

    new_lists: list[list] = []
    for lst in lists:
        new_lists.append(lst)
        for _ in range(max_len - len(new_lists[-1])):
            new_lists[-1].append(None)

    out: list[tuple] = []
    for lst in new_lists:
        out.append(tuple(ele for ele in lst))
    return out


def ex11(lst: list[tuple[str, ...]]) -> list[tuple[str, ...]]:
    return sorted(lst, key=lambda x: x[1][2])


def ex12(words: list[str]) -> list[list[str]]:
    rhymes: dict[str, str] = {}

    for i in range(len(words) - 1):
        for j in range(i, len(words)):
            if words[i] != words[j] and words[i][-2:] == words[j][-2:]:
                rhymes[words[i]] = words[j]

    return [[word, rhymes[word]] for word in rhymes]
