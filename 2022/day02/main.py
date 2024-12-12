SCORE_WINNER = 6
SCORE_DRAW = 3

ROCK = 1
PAPER = 2
SCISSORS = 3

SHAPE_SCORE = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}
SHAPE_BEATS = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}
SHAPE_BEATEN_BY = {v: k for k, v in SHAPE_BEATS.items()}
DATA_TRANSLATION = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'Y': PAPER,
    'X': ROCK,
    'Z': SCISSORS,
}


rounds = []
with open('data.txt') as file:
    rounds = [line.split() for line in file.readlines()]


def find_my_shape(opponent_shape, second_column, part_one=True):
    if part_one:
        return DATA_TRANSLATION[second_column]

    if second_column == 'X':
        return SHAPE_BEATS[opponent_shape]
    elif second_column == 'Z':
        return SHAPE_BEATEN_BY[opponent_shape]

    return opponent_shape

def play_rounds(rounds, part_one=True):
    score = 0
    for opponent, me in rounds:
        opponent_shape = DATA_TRANSLATION[opponent]
        my_shape = find_my_shape(opponent_shape, me, part_one=part_one)
        if opponent_shape == my_shape:
            score += SCORE_DRAW
        elif SHAPE_BEATS[my_shape] == opponent_shape:
            score += SCORE_WINNER

        score += SHAPE_SCORE[my_shape]

    return score


print(f'Total score part 1: {play_rounds(rounds)}')
print(f'Total score part 2: {play_rounds(rounds, False)}')
