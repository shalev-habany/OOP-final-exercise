import cv2
import numpy as np
from src.shapes.shape import Shape


class Canvas:
    """
    A class representing a drawing canvas.
    """

    def __init__(self, width: int = 500, height: int = 500):
        """
        Initialize a Canvas instance.

        :param width: The width of the canvas.
        :param height: The height of the canvas.
        """
        self.width = width
        self.height = height
        self.channels = 3
        self.image = np.zeros((self.height, self.width, self.channels), dtype="uint8")
        self.shapes = []

    def draw(self) -> np.ndarray:
        """
        Draw all shapes on the canvas.

        :return: The image with all shapes drawn on it.
        """
        for shape in self.shapes:
            shape.draw(self.image)
        return self.image

    def display(self) -> None:
        """
        Display the canvas in a window.
        """
        cv2.imshow("Canvas", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def add_shape(self, shape: Shape) -> None:
        """
        Add a shape to the canvas.

        :param shape: The shape to add to the canvas.
        """
        self.shapes.append(shape)
