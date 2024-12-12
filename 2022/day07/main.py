FILE_PATH = 'data.txt'


def get_data(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


class Node:
    def __init__(self, cmd_list):
        self.is_dir = is_dir
        self.size = size


data = get_data(FILE_PATH)