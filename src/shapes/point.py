from src.shapes.shape import Shape
import cv2


class Point(Shape):

    def __init__(self, x: float, y: float, line_color, image):
        self.x = x
        self.y = y
        self.line_color = line_color
        self.image = image

    def draw(self):
        cv2.circle(self.image, (int(self.x), int(self.y)), 1, self.line_color, -1)
