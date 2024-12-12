FILE_PATH = 'data.txt'


def extract_line_data(line):
    sectons = line.split(',')
    split_sections = (section.strip().split('-') for section in sectons)
    return [{'start': int(start), 'end': int(end)} for start, end in split_sections]


def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [extract_line_data(line) for line in lines]


def sections_contained(pair):
    section1, section2 = pair
    if section1['start'] == section2['start']:
        return True
    elif section1['start'] < section2['start']:
        return section1['end'] >= section2['end']
    
    return section1['end'] <= section2['end']


def sections_overlap(pair):
    section1, section2 = pair
    if section2['start'] <= section1['start'] <= section2['end']:
        return True
    elif section2['start'] <= section1['end'] <= section2['end']:
        return True
    return section1['start'] < section2['start'] and section1['end'] > section2['end']

data = read_data(FILE_PATH)
fully_contained = [pair for pair in data if sections_contained(pair)]
print(f'Amount of fully contained pairs: {len(fully_contained)}')

overlaps = [pair for pair in data if sections_overlap(pair)]
for f in overlaps:
    print(f)
print(f'Amount of overlapping pairs: {len(overlaps)}')