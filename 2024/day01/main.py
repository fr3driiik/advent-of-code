from typing import Tuple, List

INPUT_FILE = 'input1.txt'


def parse_file(file) -> Tuple[List[int]]:
    left = []
    right = []
    for line in file.readlines():
        try:
            left_item, right_item = line.split()
        except ValueError:
           pass
            
        left.append(int(left_item))
        right.append(int(right_item))

    return left, right


def part_one(left_list, right_list):
    left_list = sorted(left_list)
    right_list = sorted(right_list)

    distance = 0
    for left, right in zip(left_list, right_list):
        distance += abs(left - right)

    print(f'Part 1: Distance: {distance}')


def part_two(left_list, right_list):
    similarity_score = 0
    valid_right_items = (item for item in right_list if item in left_list)
    for item in valid_right_items:
        similarity_score += item

    print(f'Part 2: Similarity score: {similarity_score}')


def main() -> None:
    with open(INPUT_FILE, 'r') as file:
        left, right = parse_file(file)

    part_one(left, right)
    part_two(left, right)


if __name__ == '__main__':
    main()

