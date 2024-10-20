import cv2
import numpy as np
from src.shapes.shape import Shape


class Canvas:
    def __init__(self, width: int = 500, height: int = 500):
        self.width = width
        self.height = height
        self.channels = 3
        self.image = np.zeros((self.height, self.width, self.channels), dtype="uint8")
        self.shapes = []

    def draw(self) -> np.ndarray:
        for shape in self.shapes:
            shape.draw(self.image)
        return self.image

    def display(self) -> None:
        cv2.imshow("Canvas", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def add_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)
