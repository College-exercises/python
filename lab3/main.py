from exercices import *


def main():
    print(ex1([1, 2, 3, 4], [2, 3, 4]))
    print(ex2("Ana has apples"))
    print(
        ex3(
            {"1": "2", "list": [1, 2, 3, {"key": "val"}]},
            {"1": "2", 4: 2, "list": [1, 2, 3]},
        )
    )
    print(
        ex4(
            "a",
            "Hello there",
            href="http://python.org",
            _class="my-link",
            id="someid",
        )
    )
    print(
        ex5(
            {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
            {"key1": "come inside, it's too cold out", "key3": "this is not valid"},
        )
    )
    print(ex6([1, 2, 3, 4, 1]))
    print(ex7({1, 2}, {2, 3}))
    print(
        ex8(
            {
                "start": "a",
                "b": "a",
                "a": "6",
                "6": "z",
                "x": "2",
                "z": "2",
                "2": "2",
                "y": "start",
            }
        )
    )
    print(ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5))


if __name__ == "__main__":
    main()
