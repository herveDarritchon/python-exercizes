import string


def get_lines_from_file():
    read_lines = []
    f = open("message-plie.txt", "r")
    if f.mode == 'r':
        lines = f.readlines()
        [read_lines.append(line.rstrip()) for line in lines]
    f.close()
    return read_lines


def create_char_dict():
    cpt: int = 0
    char_dict = {}
    char_dict.update({' ': cpt})
    alphabet = string.ascii_uppercase[:26]
    for idx, char in enumerate(alphabet):
        char_dict.update({char: idx + 1})
    return char_dict


def split_in_two_parts(lines):
    line_size = len(lines[0])
    lefts, rights = [], []
    for line_idx, line in enumerate(lines):
        left, right = split_a_line_in_two_parts(line, line_size)
        lefts.append(left)
        rights.append(right)
    return lefts, rights


def split_a_line_in_two_parts(line, line_size):
    left, right = [], []
    for char_idx, char in enumerate(line):
        target = left if char_idx < line_size / 2 else right
        target.append(char)
    return left, right


def zip_lefts_and_rights_array(lefts, rights):
    return [list(zip(lefts[idx], rights[idx])) for idx in range(len(lefts))]


def sum_lefts_and_rights(zipped_array, char_dict):
    return [[((char_dict.get(l) + char_dict.get(r)), l) for l, r in line] for line in zipped_array]


def filter_26_value(sum_array):
    flatten_list = [val for sublist in sum_array for val in sublist]
    result = [v for k, v in flatten_list if k == 26]
    return "".join(result)


def decode_message():
    char_dict = create_char_dict()
    lines = get_lines_from_file()
    lefts, rights = split_in_two_parts(lines)
    zipped_array = zip_lefts_and_rights_array(lefts, rights)
    sum_array = sum_lefts_and_rights(zipped_array, char_dict)
    print(filter_26_value(sum_array))


if __name__ == "__main__":
    # execute only if run as a script
    decode_message()
