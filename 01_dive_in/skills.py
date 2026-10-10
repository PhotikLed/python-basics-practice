"""Тема: Погружение в Python.

Задача: анализ популярности навыков среди питонистов.
"""

bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34


def analyze_skills():
    """Находит минимальную и максимальную популярность навыка и выводит результат."""
    # Собираем значения всех навыков в кортеж для поиска экстремумов
    all_skills = (
        bash,
        c_and_c_plus_plus,
        c_sharp,
        html_css,
        java,
        javascript,
        sql
    )

    min_val = min(all_skills)
    max_val = max(all_skills)

    # Вывод строго по формату из условия задачи
    print(f'Доля питонистов, у которых есть наименее популярный навык (в %): {min_val}')
    print(f'Доля питонистов, у которых есть наиболее популярный навык (в %): {max_val}')


if __name__ == '__main__':
    analyze_skills()
