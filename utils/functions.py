import json
import os
from datetime import datetime
from pathlib import Path


def json_operations():
    """
    преобразует исходный файл *.json
    """
    root_path = Path(__file__).parent.parent
    operations_json = root_path.joinpath('operations.json')
    with open(operations_json, 'r', encoding='utf-8') as file:
        operation_convert = json.load(file)
    return operation_convert


def sort_operations(file_convert):
    """
    сортирует по значению  "EXECUTED" и времени
    возврвщает  пять последних по времени успешные операции
    """
    operations_good = [i for i in file_convert if i.get('state') == 'EXECUTED']
    operations_good.sort(key=lambda x: x['date'], reverse=True)
    operations_good = operations_good[:5]
    return operations_good


def transform_time(data_cor):
    """
    преобразует вывод времени операции
    """
    date_iso = datetime.fromisoformat(data_cor)
    time_cor = date_iso.date().strftime('%d.%m.%Y')
    return time_cor


def transform_number(data_correct):
    """
    зашифровывает данные кредитной карты и счета
    """
    if data_correct is None:
        private_number = ''
    elif len(data_correct.split()[-1]) != 16:
        private_number = "**" + data_correct.split()[-1][-4:]
        private_number = (' '.join(data_correct.split()[:-1]) + " " + private_number)
    else:
        card_number = data_correct.split()[-1]
        private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        piece, piece_size = len(private_number), len(private_number) // 4
        private_number = (" ".join([private_number[i:i + piece_size] for i in range(0, piece, piece_size)]))
        private_number = (' '.join(data_correct.split()[:-1]) + " " + private_number)
    return private_number


def print_result(data_cor):
    """
    распечатывает результат
    """
    time_res = transform_time(data_cor['date'])
    private_account = transform_number(data_cor.get('to'))
    private_number = transform_number(data_cor.get('from'))
    print(f"\n{time_res} {data_cor['description']}")
    print(f"{private_number } -> {private_account}")
    print(f"{data_cor['operationAmount']['amount']} {data_cor['operationAmount']['currency']['name']}")
