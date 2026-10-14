"""Тема: Итерации и циклы.

Задача: отчет по фасовке пирожных по коробкам на 3 и 5 штук.
Диапазон перебирается от заданного числа до единицы с шагом -1.
"""


def print_pack_report(starting_value: int) -> None:
    """Выводит построчный отчет о возможности фасовки пирожных от starting_value до 1.

    :param starting_value: начальное количество пирожных (> 1)
    """
    # Идем от starting_value до 1 включительно с отрицательным шагом
    for number in range(starting_value, 0, -1):
        # Число делится и на 3, и на 5 (т.е. на 15)
        if number % 3 == 0 and number % 5 == 0:
            print(f'{number} - расфасуем по 3 или по 5')
        # Делится только на 5
        elif number % 5 == 0:
            print(f'{number} - расфасуем по 5')
        # Делится только на 3
        elif number % 3 == 0:
            print(f'{number} - расфасуем по 3')
        # Не делится ни на 3, ни на 5
        else:
            print(f'{number} - не заказываем!')


if __name__ == '__main__':
    # Демонстрационный запуск
    print_pack_report(6)
    print('---')
    print_pack_report(31)
