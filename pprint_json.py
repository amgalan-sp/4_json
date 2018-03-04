import json


def load_data(filepath):
    with open(filepath, 'r', encoding="Latin-1") as file_handler:
        data1=json.load(file_handler)
        return data1

def pretty_print_json(data):
    from pprint_json import load_data
    data = str(input("Введите путь к файлу без кавычек, включая расширение: ", ))
    game = (load_data(data))
    rule = json.dumps(game, ensure_ascii=False, sort_keys=True, indent=4)
    print(rule)


if __name__ == '__main__':
    print(pretty_print_json(load_data))
