from typing import List

FILEPATH = "data/day07-1_input.txt"


def decode_rule(rule: str) -> dict:
    contains = rule.split(" contain ")[0].replace(' bags', '')
    bags = [(bag.split(' ')[0].replace('no', '0'), " ".join(bag.split(' ')[1:]))
            for bag in
            rule.split(" contain ")[1].replace('.', '').replace(' bags', '').replace(' bag', '').split(', ')]

    return {contains: bags}


def get_contained(contains: dict) -> dict:
    my_inverted_dict = dict()
    for key, value in contains.items():
        for item in value:
            my_inverted_dict.setdefault(item[1], list()).append(key)
    return my_inverted_dict


def get_contains(a_rules: List[str]) -> dict:
    out_in = {}
    for rule in a_rules:
        oi = decode_rule(rule)
        out_in.update(oi)
    return out_in


def get_all_contains(contained: dict, bag: str) -> list:
    if not bag:
        return []
    return contained.get(bag, []) + [item for b in contained.get(bag, []) for item in get_all_contains(contained, b)]


def count_all_contained(contains: dict, bag: str) -> int:
    if not bag:
        return 0
    current = sum([int(tuples[0]) for tuples in contains.get(bag, [('0', '')])])
    deep = [int(tuples[0]) * count_all_contained(contains, tuples[1]) for tuples in contains.get(bag, [(0, '')])]
    return current + sum(deep)


rules = [line.strip() for line in open(FILEPATH, 'r').readlines()]
contains = get_contains(rules)
contained = get_contained(contains)
print(len(set(get_all_contains(contained, 'shiny gold'))))
print(count_all_contained(contains, 'shiny gold'))
