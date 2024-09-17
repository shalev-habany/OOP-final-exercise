from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def rotate(self, angle):
        pass

    @abstractmethod
    def translate(self, x_offset, y_offset):
        pass

    @abstractmethod
    def scale(self, factor):
        pass