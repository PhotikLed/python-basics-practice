"""Тема: Импортируемые типы данных.

Задача: расчет дня недели на послезавтра для клуба RockRun.
Используются datetime и timedelta из стандартной библиотеки.
"""

from datetime import datetime, timedelta

WEEKDAYS = (
    'понедельник',
    'вторник',
    'среда',
    'четверг',
    'пятница',
    'суббота',
    'воскресенье',
)


def get_weekday_name(weekday_number: int) -> str:
    """Возвращает русское название дня недели по его номеру (0-6)."""
    if 0 <= weekday_number < len(WEEKDAYS):
        return WEEKDAYS[weekday_number]
    raise ValueError(f'Некорректный номер дня недели: {weekday_number}')


def get_day_after_tomorrow(date_string: str) -> str:
    """Принимает дату в формате ГГГГ-ММ-ДД и возвращает сформированную строку с днями недели."""
    # Преобразуем строку в объект datetime
    current_date = datetime.strptime(date_string, '%Y-%m-%d')
    today_weekday = get_weekday_name(current_date.weekday())

    # Вычисляем дату через 2 дня
    target_date = current_date + timedelta(days=2)
    target_weekday = get_weekday_name(target_date.weekday())

    return (
        f'Сегодня {date_string}, {today_weekday}, '
        f'а послезавтра - {target_weekday}.'
    )


if __name__ == '__main__':
    # Тестовые запуски для проверки
    for day in range(1, 7):
        print(get_day_after_tomorrow(f'2024-01-0{day}'))
