import json


def load_data(filepath):
    with open(filepath, 'r', encoding="Latin-1") as file_handler:
        return json.load(file_handler)

from pprint_json import load_data

def pretty_print_json(data):
    filepath = input("Введите путь к файлу без кавычек, включая расширение: ", )
    data = (load_data(filepath))
    print (json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    print(pretty_print_json(load_data))
