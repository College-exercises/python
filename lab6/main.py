from exercices import *


def main():
    big_text = ""
    with open("lab6/lorem.txt", "r") as file:
        big_text = file.read()
    print(ex1(big_text))
    print(ex2(r"m$", big_text, 4))
    print(ex3(big_text, [".{8,15}", r"\w{7}"]))
    print(ex4("lab6/file.xml", {"k": "name", "v": "McDonald's"}))
    print(ex5("lab6/file.xml", {"k": "name", "v": "McDonald's"}))
    print(ex6("aaaee tttet ae at    ta aita"))
    print(ex7("1650606345845"))
    print(ex8(".", "main"))


if __name__ == "__main__":
    main()
