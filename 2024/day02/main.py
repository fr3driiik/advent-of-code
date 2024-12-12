from typing import Tuple, List

INPUT_FILE = 'input1.txt'
MIN_DIFF = 1
MAX_DIFF = 3


def parse_file(file) -> Tuple[List[int]]:
    reports = []
    for line in file.readlines():
        reports.append([int(x) for x in line.split()])

    return reports

def is_safe(
        remaining: List[int],
        previous: int=None,
        increasing: bool=None,
        damping: int=0,
):
    #print(f'Is safe?: {remaining}: {previous} {increasing} {damping}')
    if damping < 0:
        return False

    if len(remaining) == 0:
        return True

    current = remaining[0]
    if previous is None:
        return (
            is_safe(remaining[1:], previous=current, damping=damping)
            or is_safe(remaining[1:], previous=None, damping=damping-1)
        )

    diff = current - previous
    if not MIN_DIFF <= abs(diff) <= MAX_DIFF:
        return is_safe(remaining[1:], previous=previous, increasing=increasing, damping=damping-1)

    if increasing is None:
        return (
            is_safe(remaining[1:], previous=current, increasing=diff>0, damping=damping)
            or is_safe(remaining[1:], previous=previous, increasing=None, damping=damping-1)
        )

    if (diff > 0) != increasing:
        return is_safe(remaining[1:], previous=previous, increasing=increasing, damping=damping-1)

    return is_safe(remaining[1:], previous=current, increasing=increasing, damping=damping)



def part_one(reports):
    safe_reports = [report for report in reports if is_safe(report)]
    print(f'Part 1: Safe reports: {len(safe_reports)}')


def part_two(reports):
    safe_reports = [report for report in reports if is_safe(report, damping=1)]
    print(f'Part 2: "Safe" reports: {len(safe_reports)}')


def main() -> None:
    with open(INPUT_FILE, 'r') as file:
        reports = parse_file(file)

    part_one(reports)
    part_two(reports)


if __name__ == '__main__':
    main()

