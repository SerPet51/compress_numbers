import pytest

from compress_numbers import compress_numbers


@pytest.mark.parametrize(
    "data, expected",
    [
        # примеры из задания
        ([1, 1, 2, 2, 3], [1, 2, 3]),
        ([0, 0, 1, 1, 0], [0, 1, 0]),
        # граничные значения
        ([], []),
        ([5], [5]),
        ([7, 7], [7]),
        # нет дубликатов
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        # проверка идентичности
        ([4, 4, 4, 4, 4], [4]),
        # дубликаты
        ([1, 1, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 2, 2, 3], [1, 2, 3]),
        ([1, 2, 3, 3, 3], [1, 2, 3]),
        # непоследовательные повторы 
        ([1, 2, 1, 2, 1], [1, 2, 1, 2, 1]),
        ([1, 1, 2, 2, 1, 1], [1, 2, 1]),
        # отрицательные числа и ноль
        ([-1, -1, 0, 0, -1], [-1, 0, -1]),
        # плавающие числа
        ([1.5, 1.5, 2.5, 2.5, 1.5], [1.5, 2.5, 1.5]),
        # большие числа
        ([10**18, 10**18, 10**18 + 1], [10**18, 10**18 + 1]),
    ],
)
def test_compress_numbers(data, expected):
    assert compress_numbers(data) == expected


def test_does_not_mutate_input():
    data = [1, 1, 2, 2, 3]
    original = data.copy()
    compress_numbers(data)
    assert data == original


def test_returns_new_list():
    data = [1, 2, 3]
    result = compress_numbers(data)
    assert result == data
    assert result is not data


def test_accepts_tuple():
    assert compress_numbers((1, 1, 2)) == [1, 2]


def test_large_input():
    data = [i // 3 for i in range(300_000)]  
    assert compress_numbers(data) == list(range(100_000))


def test_idempotent():
    data = [1, 1, 2, 2, 1, 1, 3]
    once = compress_numbers(data)
    assert compress_numbers(once) == once


def test_no_adjacent_duplicates_in_result():
    result = compress_numbers([3, 3, 1, 1, 1, 2, 2, 3, 3])
    assert all(a != b for a, b in zip(result, result[1:]))