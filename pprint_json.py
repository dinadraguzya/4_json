import json
import sys
import os


def load_data(file_path):
    with open(file_path, 'r') as opened_file:
        return json.load(opened_file)


def pretty_print_json(json_content):
    print(json.dumps(json_content, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    file_path = sys.argv[1]
    if os.path.exists(file_path) and os.path.isfile(file_path):
        pretty_print_json(load_data(file_path))
    else:
        print("The file doesn't exist!")
