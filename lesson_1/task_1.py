"""
Практическое задание к уроку №1 курса "Базы данных и PyQt"
Студент: Максим Сапунов, Jenny6199@yandex.ru
Преподаватель: Сергей Акопович Акопян

Задача №1.
Написать функцию host_ping() в которой с помощью утилиты ping будет
проверяться доступность сетевых узлов. Аргументом функции является
список, в котором каждый сетевой узел должен быть представлен именем
хоста или ip-адрессом.
В функции необходимо перебирать ip-адреса и
проверять их доступность с выводом соответствующего сообщения
("Узел доступен", "Узел недоступен").
При этом ip-адресс сетвеого узла
должен создаваться с помощью функции ip-address().
"""

import platform
import subprocess
from pprint import pprint
from ipaddress import ip_address
from art import text2art

# Список узлов для тестирования
work_list = [
    '8.8.8.8',
    '127.16.2.27',
    'yandex.ru',
    'hello_world',
    '127.0.0.1',
    '41.14.254.11',
]


def check_ip_address(node):
    """
    Функция проверяет является ли полученная строка ip-адресом.
    В случае соответствия возвращает объект-ip_address,
    или вызывает исключение с соответствующим сообщением.
    :param node (str) - строка переданная для проверки
    :return ip_address или exception
    """
    try:
        ip_v4 = ip_address(node)
        print(f'{node} - корректный ip-адрес')
    except ValueError:
        raise Exception(f'{node} - не являтеся ip-адресом')
    return ip_v4


def host_ping(node_list, show_result=False):
    """
    Функция проверяет доступность сетевых узлов посредством утилиты ping
    Каждый узел проверяется в отдельном процессе.
    :param node_list - список узлов
    :param show_result - bool - вывод на дисплей промежуточных результатов.
    """

    print(text2art('---IP-checker---'))
    print('\n', 'Программа проверки доступности узлов', '\n', '=' * 50, '\n', )

    # Словарь с результатами проверки узлов
    result = {
        'Доступные адреса': [],
        'Недоступные адреса': [],
    }
    # В цикле проверяем узлы и формируем процессы
    for node in node_list:
        try:
            ipv4 = check_ip_address(node)
        except Exception as e:
            print(f'{e}, будет проверен как доменное имя')
            ipv4 = node

        param = '-n' if platform.system().lower() == 'windows' else '-c'

        response = subprocess.Popen(
            ["ping", param, '1', '-w', '1', str(ipv4)],
            stdout=subprocess.DEVNULL,
        )

        if response.wait() == 0:
            result['Доступные адреса'].append(str(ipv4))
            report = f'{ipv4} - узел доступен. \n'
        else:
            result['Недоступные адреса'].append(str(ipv4))
            report = f'{ipv4} - узел недоступен. \n'
        if show_result:
            print(report)

    if show_result:
        print('\n', 'Результаты проверки:', '\n', '=' * 50, '\n', )
        pprint(result)
    return result


if __name__ == '__main__':
    host_ping(work_list, show_result=True)
