FILEPATH = "data/day06-1_input.txt"


def get_yes_answers_any(group_answers: list) -> list:
    return [len({a for answers in ga for a in answers}) for ga in group_answers]


def get_yes_answers_every(group_answers: list) -> list:
    response = []
    for ga in group_answers:
        every_yes = set(ga[0])
        for answers in ga:
            every_yes = every_yes.intersection(set(answers))
        response.append(len(every_yes))
    return response


the_group_answers = [line.replace('\n', ' ').split(' ') for line in open(FILEPATH, 'r').read().split('\n\n')]
print(sum(get_yes_answers_any(the_group_answers)))
print(sum(get_yes_answers_every(the_group_answers)))
