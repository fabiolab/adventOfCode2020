import csv
import re

FILEPATH = "data/day02-1_input.txt"


def decode_rule(rule: str) -> tuple:
    rule_items = rule.split()
    first_int = int(rule_items[0].split('-')[0])
    second_int = int(rule_items[0].split('-')[1])
    letter = rule_items[1]
    return letter, first_int, second_int


def is_policy01_valid(row: list) -> bool:
    letter, min, max = decode_rule(row[0])
    passwd = row[1].trim()
    return max >= len([l for l in passwd if l == letter]) >= min


def is_policy02_valid(row: list) -> bool:
    letter, pos1, pos2 = decode_rule(row[0])
    passwd = row[1].lstrip()
    ocurrencies = [m.start() for m in re.finditer(letter, passwd) if m.start() in [pos1 - 1, pos2 - 1]]
    if len(ocurrencies) != 1:
        return False
    return (pos1 - 1) in ocurrencies or (pos2 - 1) in ocurrencies


if __name__ == "__main__":
    with open(FILEPATH, 'r') as fp:
        csv_reader = csv.reader(fp, delimiter=":")
        count = 0
        for row in csv_reader:
            if is_policy02_valid(row):
                count += 1

    print(count)
