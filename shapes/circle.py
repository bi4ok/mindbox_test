import math
from typing import List, Union
from shapes.base_shape import BaseFigure


class Circle(BaseFigure):
    """
    Класс окружности с возможностью проверить корректность радиуса и вычислить площадь.
    """

    def __init__(self, radius: Union[int, float]) -> None:
        """
        Конструктор класса Circle.

        :param radius: радиус окружности
        """
        self.__radius: Union[int, float] = radius
        self.__area: float = 0
        self.__update_state()

    @property
    def area(self) -> float:
        """
        Возвращаем площадь круга
        """
        return self.__area

    @property
    def radius(self) -> Union[int, float]:
        """
        Возвращаем радиус круга
        """
        return self.__radius

    @radius.setter
    def radius(self, new_radius: Union[int, float]) -> None:
        """
        Устанавливаем новый радиус и обновляем состояние фигуры
        :param new_radius:
        """
        self.__radius = new_radius
        self.__update_state()

    def __update_state(self) -> None:
        """
        Проверка сторон, проверка является ли треугольник прямоугольным и подсчёт площади
        :return:
        """
        self.__check_radius()
        self.__area: float = self._calc_area()

    def __check_radius(self) -> None:
        """
        Проверяет корректность значения радиуса.

        Радиус должен быть положительным числом.
        """
        if not isinstance(self.__radius, (int, float)):
            raise TypeError("Стороны должны быть числами int/float")

        if self.__radius <= 0:
            raise ValueError("Радиус введен некорректно.")

    def _calc_area(self) -> float:
        """
        Вычисляет площадь круга по формуле π*r^2.
        """
        return math.pi * self.__radius ** 2
