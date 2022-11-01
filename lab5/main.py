import utils

import app


def main():
    # number = int(input("process_item input: "))
    # print(utils.process_item(number))
    print(utils.ex2_anon_func(1, 2, c=3, d=4))
    print(utils.ex2_named_func(1, 2, c=3, d=4))
    print(utils.ex3("Programming in Python is fun"))
    print(
        utils.ex4(
            {1: 2, 3: 4, 5: 6},
            {"a": 5, "b": 7, "c": "e"},
            {2: 3},
            [1, 2, 3],
            {"abc": 4, "def": 5},
            3764,
            dictionar={"ab": 4, "ac": "abcde", "fg": "abc"},
            test={1: 1, "test": True},
        )
    )
    print(utils.ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
    print(utils.ex6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

    def sum_digits(x):
        return sum(map(int, str(x)))

    print(
        utils.ex7(
            filters=[
                lambda item: item % 2 == 0,
                lambda item: item == 2 or 4 <= sum_digits(item) <= 20,
            ],
            limit=2,
            offset=2,
        )
    )
    # augmented_multiply_by_two = utils.ex8(utils.multiply_by_two)
    # print(augmented_multiply_by_two(10))
    print(utils.ex9([(5, 2), (19, 1), (30, 6), (2, 2)]))


if __name__ == "__main__":
    main()
