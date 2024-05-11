import pytest
from program import NumberList as avg


def test_UnitNumberLists():
    assert avg.get_average([1, 3, 5]) == 3
    assert avg.get_average([-2]) == -2
    assert avg.get_average([]) == 0


def test_UnitNumberListType():
    with pytest.raises(TypeError):
        avg.get_average(["Fdsdsdfsd", "fd", "fdds"])


def test_NumberListsEquals(capsys):
    expected = "Средние значения равны"
    avg.list_comparing([14, 68, 8, 10], [34, 19, 90, 1, -19])
    gotOutput = capsys.readouterr()
    assert gotOutput.out.strip() == expected


def test_NumberListsGreater(capsys):
    expected = "Первый список имеет большее среднее значение"
    avg.list_comparing([14, 68, 8, 10, 391], [34, -2, 19, 90, 1, -19])
    gotOutput = capsys.readouterr()
    assert gotOutput.out.strip() == expected


def test_NumberListsLess(capsys):
    expected = "Второй список имеет большее среднее значение"
    avg.list_comparing([14, 68, 1, 8, 10], [34, 19, 90, 1, 1019])
    gotOutput = capsys.readouterr()
    assert gotOutput.out.strip() == expected


def test_ListsComparingType():
    with pytest.raises(Exception):
        avg.list_comparing(["anyonhaseyo"], [1, 2, 3])
