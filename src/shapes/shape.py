from abc import ABC, abstractmethod

from src.shapes.point import Point


class Shape(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def rotate(self, angle: float) -> None:
        pass

    @abstractmethod
    def translate(self, x_offset: float, y_offset: float) -> None:
        pass

    @abstractmethod
    def scale(self, factor: float) -> None:
        pass

    def get_points_list(self) -> list[Point]:
        pass

    def get_center(self) -> Point:
        pass
