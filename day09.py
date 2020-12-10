import math

FILEPATH = "data/day01-1_input.txt"


def get_combinations_matching_sum(a_list: list, target: int) -> tuple:
    for i, x in enumerate(a_list):
        for j, y in enumerate(a_list[i + 1:]):
            for z in a_list[i + j + 1:]:
                if (x + y + z) == target:
                    return x, y, z


if __name__ == "__main__":
    numbers = [int(x) for x in open(FILEPATH, 'r')]
    print(math.prod(get_combinations_matching_sum(numbers, 2020)))
