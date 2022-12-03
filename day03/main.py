FILE_NAME = 'data.txt'
ASCII_LOWER_PRIORITY_OFFSET = 96
ASCII_UPPER_PRIORITY_OFFSET = 38

ELF_GROUP_SIZE = 3


def read_rucksacks(file_path):
    with open(file_path, mode='r') as file:
        return [l.strip() for l in file.readlines()]


def find_intersection(*sets):
    result = sets[0]
    for set in sets[1:]:
        result = result.intersection(set)
    
    return result


def get_item_priority(item):
    priority_offset = ASCII_UPPER_PRIORITY_OFFSET if item.isupper() else ASCII_LOWER_PRIORITY_OFFSET
    return ord(item) - priority_offset


rucksacks = read_rucksacks(FILE_NAME)
priority_total = 0
for rucksack in rucksacks:
    items_count = int(len(rucksack) / 2)
    first_compartment = {*rucksack[:items_count]}
    second_compartment = {*rucksack[-items_count:]}
    misplaced_items = find_intersection(first_compartment, second_compartment)
    for misplaced_item in misplaced_items:
        priority_total += get_item_priority(misplaced_item)

print(f'Total priority of misplaced items: {priority_total}.')


badge_priority_total = 0
for i in range(0, len(rucksacks), ELF_GROUP_SIZE):
    group_rucksacks = rucksacks[i:i+ELF_GROUP_SIZE]
    badge_items = find_intersection(*[{*rucksack} for rucksack in group_rucksacks])
    for badge_item in badge_items:
        badge_priority_total += get_item_priority(badge_item)

print(f'Total priority of badge items: {badge_priority_total}.')