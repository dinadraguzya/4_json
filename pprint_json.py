import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as opened_file:
        return json.load(opened_file)


def pretty_print_json(json_file):
    print(json.dumps(json_file, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))