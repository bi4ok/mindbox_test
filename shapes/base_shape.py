
from abc import ABC, abstractmethod


class BaseFigure(ABC):

    @abstractmethod
    def _calc_area(self) -> float:
        """Абстрактный метод для расчета площади фигуры."""
        pass

    @abstractmethod
    def area(self) -> float:
        pass