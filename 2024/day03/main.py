import re
import functools


FILE_NAME = "input1.txt"


def part_one(data):
    matches = re.findall(r"mul\(([\d]{1,3}),([\d]{1,3})\)", data)
    sum = functools.reduce(lambda a, b: a + int(b[0]) * int(b[1]), matches, 0)
    print(f'Part one: {sum}')


def part_two(data):
    matches = re.findall(r"mul\(([\d]{1,3}),([\d]{1,3})\)|(do\(\))|(don't\(\))", data)
    sum = 0
    enabled = True
    for v1, v2, cmd_do, cmd_dont in matches:
        if cmd_do:
            enabled = True
        elif cmd_dont:
            enabled = False
        elif enabled:
            sum += int(v1) * int(v2)

    print(f'Part two: {sum}')

def main():
    with open(FILE_NAME, "r") as file:
        data = file.read()

    part_one(data)
    part_two(data)


if __name__ == "__main__":
    main()
