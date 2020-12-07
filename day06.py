from typing import List

FILEPATH = "data/day04-1_input.txt"

REQUIERED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

CHECK = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: 150 <= int(x[:3]) <= 193 and 'cm' in x or 59 <= int(x[:2]) <= 76 and 'in' in x,
    "hcl": lambda x: x[0] == '#' and bool(int(x[1:], 16)),
    "ecl": lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    "pid": lambda x: bool(int(x[1:])),
    "cid": lambda x: True
}


def check_fieldvalue(field: str) -> bool:
    try:
        return CHECK[field.split(':')[0]](field.split(':')[1])
    except Exception:
        return False


def check_fields(passports: List[List[str]]):
    return [set([item.split(':')[0] for item in passport]).intersection(REQUIERED_FIELDS) == REQUIERED_FIELDS for
            passport in passports]


the_passports = [line.replace('\n', ' ').split(' ') for line in open(FILEPATH, 'r').read().split('\n\n')]
ok_passports = [a_passport for a_passport in the_passports if all([check_fieldvalue(field) for field in a_passport])]
print(len([field for field in check_fields(the_passports) if field]))
print(len(ok_passports))
