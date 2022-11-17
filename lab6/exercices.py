import os
import re

from bs4 import BeautifulSoup


def ex1(text: str) -> list[str]:
    return [
        word
        for word in re.split(r"\s+", text)
        if re.search(r"[a-z\d]+", word, re.IGNORECASE)
    ]


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
    return [str(re.findall(regex, text)) for regex in regexes]


def __has_all_tags(xml_soup: BeautifulSoup, attrs: dict[str, str]) -> bool:
    for attr in attrs:
        if not xml_soup.has_attr(attr):
            return False
        if xml_soup[attr] != attrs[attr]:
            return False
    return True


def ex4(xml_path: str, attrs: dict[str, str]) -> list[str]:
    if not os.path.exists(xml_path):
        raise ValueError(f"Path {os.path.abspath(xml_path)} does not exist")

    out: list[str] = []
    with open(xml_path, "r") as file:
        soup = BeautifulSoup(file, "xml")
        out = list(soup.find_all(attrs=attrs))
    return out


def ex5(xml_path: str, attrs: dict[str, str]) -> list[str]:
    ...


def ex6(text: str) -> str:
    matches = re.findall(r"([aeiou]\w*[aeiou])(?:(\s+|$))", text, re.IGNORECASE)
    for word, _ in matches:
        current_word = ""
        for ele in word[::2]:
            current_word += ele + "*"
        if len(word) % 2 == 1:
            current_word = current_word[:-1]
        text = text.replace(word, current_word)
    return text
