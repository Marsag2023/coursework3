from utils.functions import transform_time, sort_operations, print_result, transform_number


def test_sort():
    """
    тестируем функцию сортировки по значению  "EXECUTED" и времени
    """
    file = [{'state': 'EXECUTED', 'date': '2019-12-06T22:46:21.935582'},
            {'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890'},
            {'state': 'EXECUTED', 'date': '2019-12-08T09:22:25.899614'},
            {'state': 'EXECUTED', 'date': '2019-12-09T17:38:04.800051'},
            {'state': 'EXEC', 'date': '2019-12-06T22:46:21.935582'},
            {'state': 'EXECUTED', 'date': '2019-12-10T12:04:13.781725'}]
    assert sort_operations(file) == [
            {'state': 'EXECUTED', 'date': '2019-12-10T12:04:13.781725'},
            {'state': 'EXECUTED', 'date': '2019-12-09T17:38:04.800051'},
            {'state': 'EXECUTED', 'date': '2019-12-08T09:22:25.899614'},
            {'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890'},
            {'state': 'EXECUTED', 'date': '2019-12-06T22:46:21.935582'}]


def test_transform():
    """
    тестируем функцию вывода времени операции
    """
    test_time = '2019-12-06T22:46:21.935582'
    assert transform_time(test_time) == "06.12.2019"


def test_number():
    """
    тестируем функцию шифровки  данных кредитной карты и счета

    """
    assert transform_number(None) == ""
    assert transform_number('Maestro 1596837868705199') == "Maestro 1596 83** **** 5199"
    assert transform_number('Счет 64686473678894779589') == "Счет **9589"


def test_print():
    """

    :return:
    """
    data_cor = {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
     'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}
    print_result(data_cor)
    #assert print_result(data_cor) == ["08.12.2019 Открытие вклада", " -> Счет **5907", "41096.24 USD"]