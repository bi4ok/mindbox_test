import math
from typing import List, Union
from functools import reduce
from shapes.base_shape import BaseFigure


class Triangle(BaseFigure):
    """
    Класс треугольника с возможностью проверить правильность сторон,
    вычислить площадь и определить наличие прямого угла.
    """

    def __init__(self, new_sides: List[Union[int, float]]) -> None:
        """
        Конструктор класса Triangle.

        :param new_sides: список длин всех сторон
        """
        self.__sides: List[Union[int, float]] = sorted(new_sides)
        self.__right_angled: bool = False
        self.__area: float = 0
        self.__update_state()  # Считаем значения при смене, чтобы не пересчитывать их каждый раз

    @property
    def is_right_angled(self) -> bool:
        """
        Возвращает True если треугольник прямоугольный
        """
        return self.__right_angled

    @property
    def area(self) -> float:
        """
        Возвращает посчитанную площадь треугольника
        """
        return self.__area

    @property
    def figure_sides(self) -> List[Union[int, float]]:
        """
        Возвращает стороны треугольника
        """
        return self.__sides

    @figure_sides.setter
    def figure_sides(self, new_sides: List[Union[int, float]]) -> None:
        """
        Меняет стороны треугольника на новые. Выполняет проверку новых сторон и обновляет атрибуты
        :param new_sides:
        """
        self.__sides: List[Union[int, float]] = sorted(new_sides)
        self.__update_state()

    def __update_state(self):
        """
        Проверка сторон, проверка является ли треугольник прямоугольным и подсчёт площади
        :return:
        """
        self.__check_sides()
        self.__right_angled: bool = self.__check_right()
        self.__area: float = self._calc_area()

    def __check_sides(self) -> None:
        """
        Метод проверяет корректность введенных значений сторон треугольника.

        Выкидывает исключение, если стороны введены неправильно.
        """
        if not all([isinstance(side, (int, float)) for side in self.__sides]):
            raise TypeError("Стороны должны быть числами int/float")

        if len(self.__sides) != 3:
            raise ValueError("Сторон должно быть 3")

        if min(self.__sides) <= 0:
            raise ValueError("Стороны должны быть больше 0")

        a, b, c = self.__sides
        two_sides_check = (a + b) <= c or (a + c) <= b or (b + c) <= a
        if two_sides_check:
            raise ValueError("Сумма длин двух сторон должна быть больше длины третьей стороны")

    def _calc_area(self) -> float:
        """
        Вычисляет площадь треугольника методом Герона.

        Формула Герона: sqrt(s*(s-a)*(s-b)*(s-c)), где s - полупериметр.
        """
        semi_perimeter = sum(self.__sides) / 2
        aux_values = [semi_perimeter] + [semi_perimeter - side for side in self.__sides]
        return math.sqrt(reduce(lambda x, y: x * y, aux_values))

    def __check_right(self) -> bool:
        """
        Определяет, является ли треугольник прямоугольным.

        Треугольник считается прямоугольным, если выполняется теорема Пифагора с заданной точностью.
        """
        hypotenuse_squared = max(self.__sides) ** 2
        other_sides_squared_sum = sum(map(lambda x: x ** 2, filter(lambda x: x != max(self.__sides), self.__sides)))
        return math.isclose(hypotenuse_squared, other_sides_squared_sum)

