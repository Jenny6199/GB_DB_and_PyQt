"""
Практическое задание к уроку №1 курса "Базы данных и PyQt"
Студент: Максим Сапунов, Jenny6199@yandex.ru
Преподаватель: Сергей Акопович Акопян

Задача №2
Написать функцию host_range_ping() для перебора ip-адресов из заданного
диапазона. Меняться должен только последний октет каждого адерса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

from task_1 import check_ip_address, host_ping


def host_range_ping(show_result=True):
    """
    Запрашивает адрес и количество необходимых доступных адресов
    Если в последнем октете есть возможность увеличивать номер адреса,
    то проверяет их доступность и возвращает список доступных адресов.
    :param show_result - bool - выключатель вывода информационных сообщений.
    :return
    """
    while True:
        print('Будет выполнена последовательная проверка IP-адресов:')
        ip_start = input('Введите начальный адрес:')
        try:
            ipv4_start = check_ip_address(ip_start)
            last_octet = int(ip_start.split('.')[3])
            break
        except Exception as e:
            print(e)

    while True:
        number_of_node = input('Необходмое количество адерсов: ')
        if not number_of_node.isnumeric():
            print('Необходимо ввести число.')
        else:
            if last_octet + int(number_of_node) > 256:
                print('Можем изменить только последний октет.', )
                number_of_node = 256 - last_octet
                print(f'Количество адресов - {number_of_node}')
                break
            else:
                break

    checking_hosts = []
    [checking_hosts.append(str(ipv4_start + el)) for el in range(int(number_of_node))]
    return host_ping(checking_hosts, show_result)


if __name__ == '__main__':
    host_range_ping()
