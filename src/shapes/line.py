import cv2

from src.shapes.point import Point
from src.shapes.shape import Shape


class Line(Shape):

    def __init__(self, x1: float, y1: float, x2: float, y2: float, line_color, image):
        self.point1 = Point(x1, y1, line_color, image)
        self.point2 = Point(x2, y2, line_color, image)
        self.line_color = line_color
        self.image = image
        self.center_x = (self.point1.x + self.point2.x) / 2
        self.center_y = (self.point1.y + self.point2.y) / 2

    def draw(self):
        cv2.line(self.image, (int(self.point1.x), int(self.point1.y)), (int(self.point2.x), int(self.point2.y)), self.line_color, 1)

    def rotate(self, angle):
        rotation_matrix = cv2.getRotationMatrix2D((self.center_x, self.center_y), angle, 1)
        self.apply_operation_matrix(rotation_matrix)

    def translate(self, x_offset, y_offset):
        self.point1.translate(x_offset, y_offset)
        self.point2.translate(x_offset, y_offset)

    def scale(self, factor):
        scale_matrix = cv2.getRotationMatrix2D((self.center_x, self.center_y), 0, factor)
        self.apply_operation_matrix(scale_matrix)

    def apply_operation_matrix(self, matrix):
        print(matrix.shape)
        point1_scaled = matrix @ [[self.point1.x], [self.point1.y], [1]]
        point2_scaled = matrix @ [[self.point2.x], [self.point2.y], [1]]
        self.point1.set_point(point1_scaled[0], point1_scaled[1])
        self.point2.set_point(point2_scaled[0], point2_scaled[1])
