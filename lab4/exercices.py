import os
from typing import Callable


def ex1(dir_: str) -> list[str]:
    out: set[str] = set()

    for item in os.listdir(dir_):
        if os.path.isfile(f"{dir_}/{item}"):
            _, ext = os.path.splitext(item)
            if ext != "":
                out.add(ext)

    return sorted(list(out))


def ex2(dir_: str, file: str) -> None:
    with open(file, "w", encoding="latin1") as fille:
        for item in os.listdir(dir_):
            file_path = os.path.abspath(f"{dir_}/{item}")
            if os.path.isfile(file_path) and item[0] == "A":
                fille.write(f"{file_path}{os.linesep}")


def __files_in_dir(dir_: str) -> list[str]:
    if not dir_.endswith("/"):
        dir_ += "/"
    out: list[str] = []

    for item in os.listdir(dir_):
        if os.path.isdir(dir_ + item):
            out += __files_in_dir(dir_ + item + "/")
        out.append(dir_ + item)
    return out


def ex3(path: str) -> str | list[tuple[str, int]]:
    if os.path.isfile(path):
        with open(path, "r", encoding="latin1") as file:
            return "".join(file.readlines())[-20:]

    names_ext = [os.path.splitext(path) for path in __files_in_dir(path)]

    frequency: dict[str, int] = {}
    for _, ext in names_ext:
        if ext == "":
            continue

        if ext not in frequency:
            frequency[ext] = 1
        else:
            frequency[ext] += 1

    sorted_fq = sorted(frequency, key=lambda x: frequency[x], reverse=True)
    return list((key, frequency[key]) for key in sorted_fq)


def ex4(dir_: str) -> list[str]:
    return list(item[0] for item in ex3(dir_))


def ex5(target: str, to_search: str) -> list[str]:
    return ex6(target, to_search)


def ex6(
    target: str,
    to_search: str,
    callback: Callable[[Exception], None] = Callable,
) -> list[str]:
    if os.path.isdir(target):
        search_here = __files_in_dir(target)
    elif os.path.isfile(target):
        search_here = [target]
    else:
        raise ValueError("corresponding message")

    out: list[str] = []

    for file_path in search_here:
        try:
            with open(file_path, "r", encoding="latin1") as file:
                if to_search in "".join(file.readlines()):
                    out.append(file_path)
        except Exception as ex:
            if callback is not Callable:
                callback(ex)
    return out


def ex7(file_path: str) -> dict[str, str | int | bool]:
    return {
        "full_path": os.path.abspath(file_path),
        "full_size": os.path.getsize(file_path),
        "file_extension": os.path.splitext(file_path)[1],
        "can_read": os.access(file_path, os.R_OK),
        "can_write": os.access(file_path, os.W_OK),
        "can_execute": os.access(file_path, os.X_OK),
    }


def ex8(dir_path: str) -> list[str]:
    return list(f"{os.getcwd()}/{file}" for file in __files_in_dir(dir_path))
