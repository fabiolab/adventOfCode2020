import math

FILEPATH = "data/day03-1_input.txt"


def count_char(a_map: list, searched: str, vertical_step: int, horizontal_step: int) -> int:
    if not a_map:
        return 0
    num_rows = len(a_map[0])
    return len([line for index, line in enumerate(a_map[::vertical_step]) if
                line[index * horizontal_step % num_rows] == searched])


if __name__ == "__main__":
    the_map = [line.strip() for line in open(FILEPATH, 'r')]
    trees = [count_char(the_map, '#', 1, 1),
             count_char(the_map, '#', 1, 3),
             count_char(the_map, '#', 1, 5),
             count_char(the_map, '#', 1, 7),
             count_char(the_map, '#', 2, 1),
             ]
    print(math.prod(trees))
