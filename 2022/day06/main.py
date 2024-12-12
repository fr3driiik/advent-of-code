FILE_PATH = 'data.txt'


def get_data(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def find_marker_index(message, marker_length):
    message_quads_lazy = (message[start:start+marker_length] for start in range(len(message)-marker_length))
    start = next((index for index, quad in enumerate(message_quads_lazy) if len(set(quad)) == marker_length))
    return start + marker_length

data = get_data(FILE_PATH)
start_index = find_marker_index(data, 4)
message_index = find_marker_index(data, 14)
print(start_index, message_index)