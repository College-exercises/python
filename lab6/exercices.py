import os
import re

from bs4 import BeautifulSoup


def ex1(text: str) -> list[str]:
    return re.findall(r"\b\w+[!?.]?", text)


def ex2(regex: str, text: str, x: int) -> list[str]:
    try:
        pattern = re.compile(regex)
    except re.error as ex:
        raise ValueError(f"Invalid regex argument {regex}", ex)

    return [
        word
        for word in re.split(r"\s+", text)
        if len(word) == x and re.search(pattern, word)
    ]


def ex3(text: str, regexes: list[str]) -> list[str]:
    return list(
        map(
            lambda x: x.group(0),  # type: ignore
            filter(
                lambda x: x is not None,
                (re.match(regex, text) for regex in regexes),
            ),
        )
    )


# python < 3.11
# def ex4(xml_path: str, attrs: dict[str, str]) -> list[str]:
#     if not os.path.exists(xml_path):
#         raise ValueError(f"Path {os.path.abspath(xml_path)} does not exist")

#     out: list[str] = []
#     with open(xml_path, "r") as file:
#         soup = BeautifulSoup(file, "xml")
#         current = list(soup.find_all(attrs=attrs))
#         if current:
#             out.append(current)  # type: ignore
#     return out


def __contains_one_attr(xml_line: str, attr: tuple[str, str]) -> bool:
    return re.search(rf'{attr[0]}\s*=\s*"{attr[1]}"(\s|>)', xml_line) is not None


def ex4(xml_path: str, attrs: dict[str, str], attr_count=99) -> list[str]:
    if not os.path.exists(xml_path):
        raise ValueError(f"Path {os.path.abspath(xml_path)} does not exist")

    out: list[str] = []
    with open(xml_path, "r") as file:
        for line in file.readlines():
            current_found = 0
            for attr in attrs:
                if __contains_one_attr(line, (attr, attrs[attr])):
                    current_found += 1
                    if current_found >= attr_count:
                        out.append(line.rstrip("\n").strip())
                        break

    return out


def ex5(xml_path: str, attrs: dict[str, str]) -> list[str]:
    return ex4(xml_path, attrs, 1)


def ex6(text: str) -> str:
    matches = re.findall(r"\b([aeiou]\w*[aeiou])\b", text, re.IGNORECASE)
    for word in matches:
        current_word = ""
        for ele in word[::2]:
            current_word += ele + "*"
        if len(word) % 2 == 1:
            current_word = current_word[:-1]
        text = text.replace(word, current_word)
    return text


def ex7(cnp: str) -> bool:
    if not (
        re.search(
            r"^[0-8]\d\d((0[1-9])|(1[0-2]))((0[1-9])|([12]\d)|(3[01]))\d{6}$", cnp
        )
    ):
        return False
    magic_sum = sum(
        list(
            int(zipped[0]) * int(zipped[1]) for zipped in zip("279146358279", cnp[:-1])
        )
    )
    return int(cnp[-1]) == (magic_sum % 11 if magic_sum % 11 != 10 else 1)


def ex8(dir_path: str, regex: str) -> list[str]:
    if not os.path.exists(dir_path):
        raise FileNotFoundError("Directory does not exist")
    if not os.path.isdir(dir_path):
        raise OSError(f"{dir_path} is not a directory")

    out: list[str] = []
    for dirpath, _, filenames in os.walk(dir_path):
        for file in filenames:
            if re.search(regex, file):
                try:
                    with open(f"{dirpath}/{file}", "r") as f:
                        if re.search(regex, f.read()):
                            out.append(f">>{file}")
                except UnicodeDecodeError:
                    pass
            elif re.search(regex, file):
                out.append(file)

    return out
