file_name = 'data.txt'

with open(file_name) as file:
    content = file.read()
    calories_per_elf = list((sum((int(v) for v in chunk.split())) for chunk in content.split('\n\n')))  # This line is a joke
    calories_per_elf.sort()
    answer1 = calories_per_elf[-1]
    answer2 = sum(calories_per_elf[-3:])
    print(f'Max calories carried by on elf: {answer1}')
    print(f'Total calories for top three elves: {answer2}')
