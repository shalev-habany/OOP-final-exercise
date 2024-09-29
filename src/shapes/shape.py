from abc import ABC, abstractmethod

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

    def get_points_list(self):
        pass

    def get_center(self):
        pass