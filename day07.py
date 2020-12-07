FILEPATH = "data/day05-1_input.txt"


def decode_board_pass(a_board_pass: str) -> int:
    # Hint: that's all about binary encoding! It's like searching into a binary tree
    row = int(a_board_pass[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(a_board_pass[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col


board_passes = [line.strip() for line in open(FILEPATH, 'r').readlines()]
booked_seats = sorted([decode_board_pass(bp) for bp in board_passes])
free_seats = [seat for seat, seat_next in zip(booked_seats, booked_seats[1:] + [booked_seats[0]]) if
              seat + 1 != seat_next and seat != max(booked_seats)]
print(max(booked_seats))
print(free_seats)
