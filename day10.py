FILEPATH = "data/day10-1_input.txt"

the_adapters = sorted([int(x) for x in open(FILEPATH, 'r')])


def get_adapters(adapter: int, adapters: list) -> tuple:
    if not adapters:
        return 0, 0
    if adapters[0] == adapter + 3:
        one_jolt, three_jolts = get_adapters(adapters[0], adapters[1:])
        return one_jolt, three_jolts + 1
    elif adapters[0] == adapter + 1:
        one_jolt, three_jolts = get_adapters(adapters[0], adapters[1:])
        return one_jolt + 1, three_jolts


# An adapter is optionnal if it is between two adapters that differs of 1 unit
# This function get the removable adapter, grouped as they follow each other
def get_removables_by_group(adapters: list) -> list:
    removables = []
    group = []
    for index, adapter in enumerate(adapters):
        try:
            if adapters[index - 1] + 1 == adapter == adapters[index + 1] - 1:
                group.append(adapter)
            else:
                removables.append(group)
                group = []
        except IndexError:
            removables.append(group)
            group = []
    return removables


one, three = get_adapters(0, the_adapters)
print(one * (three + 1))

removables_adapters = get_removables_by_group([0] + the_adapters)
print(removables_adapters)
count = 1
for group in removables_adapters:
    if len(group) == 1:
        count = count * 2
    if len(group) == 2:
        count = count * 4
    if len(group) == 3:
        count = count * 7
print(count)
