## project_3

# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * список из кортежа строк и кортежа вещественных чисел
#   * словарь
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any
import random 

import random 
from datetime import timedelta
from decimal import Decimal, ROUND_HALF_DOWN

playlist_d = [
    ("The Flute Tune", "Voodoo People", "Galvanize", "Miami Disco", "Komarovo", "Wild Frontier", "Check It Out", "Seasons", "These Things Will Come To Be"),
    (5.23, 5.07, 7.34, 4.31, 2.26, 4.28, 2.09, 4.25, 4.56),
]

playlist_b = {
    'Портофино': 3.32,
    'Снег': 4.35,
    'Попытка №5': 3.23,
    'Тополиный Пух': 3.53,
    'Если хочешь остаться': 4.48,
    'Зеленоглазое такси': 5.52,
    'Ты не верь слезам': 3.1,
    'Nowhere to Run': 2.58,
    'Салют, Вера': 4.44,
    'Улетаю': 3.24,
    'Опять метель': 3.37,
}

def _get_random_songs(playlist) -> dict:
    """
    TODO - опиши документацию
    """
    # TODO - Создаешь функцию, которая обрабатывает два разных плейлиста. 
    # То есть в качестве параметра можно вставить и плейлист d и плейлист b" 
    # !!! функция _get_random_songs должна возвращать словарь из n пар случайных песен
    merge_playlist = list(zip(playlist_d[0], playlist_d[1]))
    random.shuffle(merge_playlist)
    return merge_playlist[:n]

# print(get_random_songs(playlist_b, 3))


def get_duration(playlist: list|dict) -> timedelta:
    """
    Функция принимает плейлист с песнями и временем звучания в виде коллекции и возвращает время звучания

    :param playlist: исходная коллекция с песнями
    :type playlist: list|dict

    :param n: количество песен
    :type n: int

    :return: время звучания
    :rtype: timedelta
    """
    song_list: dict = _get_random_songs(playlist)  # TODO - дописать эту функцию, 
    total_time = timedelta(minutes=0, seconds=0)
    for i in song_list.values():
        round_time = Decimal(i).quantize(Decimal("1.00"), ROUND_HALF_DOWN)
        _min, _sec = str(round_time).split(".")
        res = timedelta(minutes=int(_min),seconds=int(_sec))
        total_time = total_time + res
                            
    return total_time

# вызов
n = 3
print(get_duration(playlist_d, n))
