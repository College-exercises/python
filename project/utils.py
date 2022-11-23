import os
import random
import re
import string

import requests
from bs4 import BeautifulSoup


def get_words_online() -> set[str]:
    if os.path.exists("project/online_words.txt"):
        return get_words_from_file("project/online_words.txt")

    response = requests.get(
        "https://gonaturalenglish.com/1000-most-common-words-in-the-english-language/",
        timeout=5,
    )
    if not response.ok:
        raise ConnectionError(
            f"Request to get list of words failed with code={response.status_code}"
        )

    soup = BeautifulSoup(response.content, features="html.parser")
    words_div = soup.find(attrs={"class": "elementor-element-5df9d27"})
    words_ol = str(words_div.find_all("ol")[1].text)  # type: ignore

    out: set[str] = set()
    for line in words_ol.split("\n"):
        if line != "":
            match = re.search(r"^(\w+)(\s| )", line)
            if match:
                out.add(match.group(0)[:-1])

    with open("project/online_words.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(out))

    return out


def get_words_from_file(file_path: str) -> set[str]:
    out: set[str] = set()

    with open(file_path, encoding="utf-8") as file:
        for line in file.readlines():
            for item in re.split(r"\s+", line.rstrip("\n").strip()):
                out.add(item)

    return out


def generate_password_from_words(words: set[str]) -> str:
    out = ""

    # while len(out) < 12:
    #     choice = random.choice(list(words))
    #     if len(out + choice) <= 12:
    #         out += choice

    while True:
        choice = random.choice(list(words))
        if len(out + choice) <= 12:
            out += choice
        else:
            break

    out += "".join(
        random.choices(
            string.ascii_letters + string.digits + string.punctuation,
            k=12 - len(out),
        )
    )

    return out
