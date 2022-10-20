import difflib
import json
from typing import TypeVar
from lab2 import exercices

ex1 = exercices.ex3


def ex2(string: str) -> dict[str, int]:
    out: dict[str, int] = {}

    for ch in string:
        if ch not in out:
            out[ch] = 1
        else:
            out[ch] += 1

    return out


def ex3(d1: dict, d2: dict) -> str:
    return "".join(
        difflib.context_diff(json.dumps(d1, indent=1), json.dumps(d2, indent=1))
    )


def ex4(tag: str, content: str, **key_val: str) -> str:
    return f"""<{tag} {" ".join(f'{key}="{key_val[key]}"' for key in key_val)}>{content}</{tag}>"""


def ex5(tuples: set[tuple[str, str, str, str]], d: dict[str, str]) -> bool:
    if set(ele[0] for ele in tuples) != set(d.keys()):
        return False

    dict_tuples: dict[str, tuple[str, str, str]] = {}
    for ele in tuples:
        dict_tuples[ele[0]] = (ele[1], ele[2], ele[2])
    for key in d:
        if not d[key].startswith(dict_tuples[key][0]):
            return False
        if dict_tuples[key][1] not in d[key]:
            return False
        if not d[key].endswith(dict_tuples[key][2]):
            return False

    return True


T = TypeVar("T")


def ex6(lst: list[T]) -> tuple[int, int]:
    set_lst: set[T] = set()
    duplicates = 0

    for item in lst:
        if item not in set_lst:
            set_lst.add(item)
        else:
            duplicates += 1

    return (len(lst) - duplicates, duplicates)


def ex7(*sets: set[T]) -> dict[str, set[T]]:
    out: dict[str, set[T]] = {}

    for i in range(0, len(sets) - 1):
        for j in range(i + 1, len(sets)):
            out[f"{sets[i]} | {sets[j]}"] = sets[i].union(sets[j])
            out[f"{sets[i]} & {sets[j]}"] = sets[i].intersection(sets[j])
            out[f"{sets[i]} - {sets[j]}"] = sets[i] - sets[j]
            out[f"{sets[j]} - {sets[i]}"] = sets[j] - sets[i]

    return out


def ex8(mapping: dict[str, str]) -> list[str]:
    assert "start" in mapping
    out: list[str] = []
    current_item = "start"
    while current_item not in out:
        out.append(current_item)
        current_item = mapping[current_item]
    return out[1:]


def ex9(*args, **kwargs) -> int:
    return len(set(args).intersection(set(kwargs.values())))
