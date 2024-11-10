from abc import ABC, abstractmethod

from numpy import ndarray


class Shape(ABC):

    @abstractmethod
    def draw(self, image: ndarray) -> ndarray:
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

    @abstractmethod
    def get_points_list(self):
        pass

    @abstractmethod
    def get_center(self):
        pass

    @abstractmethod
    def update_center(self):
        pass
