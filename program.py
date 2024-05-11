# Создайте программу на Python или Java, которая принимает
# два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"",
# если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"",
# если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.

# Важно:
# Приложение должно быть написано в соответствии с принципами
# объектно-ориентированного программирования.
# Используйте Pytest (для Python) или JUnit (для Java) для написания
# тестов, которые проверяют правильность работы программы. Тесты
# должны учитывать различные сценарии использования вашего приложения.
# Используйте pylint (для Python) или Checkstyle (для Java) для проверки качества кода.
# Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.

# *Формат и требования к сдаче: *
# Отчет о выполнении этого задания должен включать в себя следующие элементы:
# - Код программы
# - Код тестов
# - Отчет pylint/Checkstyle
# - Отчет о покрытии тестами
# - Объяснение того, какие сценарии покрыты тестами и почему
# вы выбрали именно эти сценарии.


class NumberList:
    def get_average(nums: list[int | float]) -> float:
        if not isinstance(nums, list):
            raise TypeError(
                f"incorrect type of data, expected type list, but got {type(nums)}"
            )
        if not nums:
            return 0
        avg = sum(nums) / len(nums)
        try:
            return avg
        except TypeError:
            print("Something went wrong, restart program and try again")

    def list_comparing(nums1: list[int | float], nums2: list[int | float]) -> None:
        first_nums_avg = NumberList.get_average(nums1)
        second_nums_avg = NumberList.get_average(nums2)
        if first_nums_avg > second_nums_avg:
            print("Первый список имеет большее среднее значение")
        elif first_nums_avg < second_nums_avg:
            print("Второй список имеет большее среднее значение")
        elif first_nums_avg == second_nums_avg:
            print("Средние значения равны")


NumberList.list_comparing([1], [2])
