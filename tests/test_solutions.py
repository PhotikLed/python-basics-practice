"""Юнит-тесты для проверки решений практических заданий по основам Python."""

import pytest
import io
import sys
from importlib import import_module

# Импортируем модули заданий
skills_module = import_module('01_dive_in.skills')
pool_module = import_module('02_branching.pool_tiles')
dates_module = import_module('03_imported_types.dates')
olympiad_module = import_module('04_collections.olympiad')
bakery_module = import_module('05_loops.bakery')


def test_analyze_skills(capsys):
    """Проверяет вывод функции analyze_skills."""
    skills_module.analyze_skills()
    captured = capsys.readouterr().out
    assert 'Доля питонистов, у которых есть наименее популярный навык (в %): 11' in captured
    assert 'Доля питонистов, у которых есть наиболее популярный навык (в %): 37' in captured


@pytest.mark.parametrize(
    'dep,leng,wid,expected',
    [
        (2, 2, None, 20),
        (2, 2, 2, 20),
        (1, 2, 3, 16),
        (2, 5, 3, 47),
        (3, 4, None, 64),
    ]
)
def test_count_tiles(dep, leng, wid, expected):
    """Проверяет расчет плитки для квадратных и прямоугольных бассейнов."""
    if wid is None:
        assert pool_module.count_tiles(dep, leng) == expected
    else:
        assert pool_module.count_tiles(dep, leng, wid) == expected


def test_weekday_names():
    """Проверяет корректное сопоставление номеров дней недели с их именами."""
    assert dates_module.get_weekday_name(0) == 'понедельник'
    assert dates_module.get_weekday_name(4) == 'пятница'
    assert dates_module.get_weekday_name(6) == 'воскресенье'
    with pytest.raises(ValueError):
        dates_module.get_weekday_name(7)


def test_day_after_tomorrow():
    """Проверяет расчет даты через 2 дня."""
    res = dates_module.get_day_after_tomorrow('2024-01-01')
    assert res == 'Сегодня 2024-01-01, понедельник, а послезавтра - среда.'

    res2 = dates_module.get_day_after_tomorrow('2024-01-06')
    assert res2 == 'Сегодня 2024-01-06, суббота, а послезавтра - понедельник.'


def test_check_winners(capsys):
    """Проверяет проверку попадания в топ-3 участников олимпиады."""
    scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28, 55]
    # Топ-3: 55, 52, 51

    olympiad_module.check_winners(scores, 52)
    out1 = capsys.readouterr().out
    assert 'Вы в тройке победителей!' in out1

    olympiad_module.check_winners(scores, 48)
    out2 = capsys.readouterr().out
    assert 'Вы не попали в тройку победителей.' in out2


def test_print_pack_report(capsys):
    """Проверяет вывод отчета по фасовке пирожных."""
    bakery_module.print_pack_report(6)
    out = capsys.readouterr().out.strip().split('\n')
    assert out == [
        '6 - расфасуем по 3',
        '5 - расфасуем по 5',
        '4 - не заказываем!',
        '3 - расфасуем по 3',
        '2 - не заказываем!',
        '1 - не заказываем!',
    ]
