from itertools import combinations

FILEPATH = "data/day09-1_input.txt"

numbers = [int(x) for x in open(FILEPATH, 'r')]

error_number = None
for index in range(len(numbers) - 24):
    preamble = numbers[index:25 + index]
    to_check = numbers[25 + index]
    combis = set([sum(num) for num in combinations(preamble, 2) if num[0] != num[1]])
    if to_check not in combis:
        error_number = to_check
        print(f"Error {to_check}")
        break

window_start_pos = 0
window_end_pos = 0
while True:
    window = numbers[window_start_pos:window_end_pos]
    current_sum = sum(window)
    if current_sum == error_number:
        print(min(window) + max(window))
    elif current_sum > error_number:
        window_start_pos += 1
        window_end_pos = window_start_pos
    else:
        window_end_pos += 1
