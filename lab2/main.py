from exercices import *


def main():
    print(ex1(10))
    print(ex2(list(range(100))))
    print(ex3([1, 2, 3, 4], [2, 3, 4]))
    print(ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    print(ex5([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(ex6([1, 1, 1], [1, 2, 1], [2, 2, 2], x=3))
    print(ex7([121, 232, 112, 242, 252]))
    print(ex8(["test", "hello", "lab002"], 2, False))
    print(
        ex9(
            [
                [1, 2, 3, 2, 1, 1],
                [2, 4, 4, 3, 7, 2],
                [5, 5, 2, 5, 6, 4],
                [6, 6, 7, 6, 7, 5],
            ]
        )
    )
    print(ex10([1, 2, 3], [5, 6, 7, 1], ["a", "b", "c"]))
    print(ex11([("abc", "bcd"), ("abc", "zza")]))
    print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))


if __name__ == "__main__":
    main()
