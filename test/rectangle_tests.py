import unittest

import numpy as np

from src.canvas import Canvas
from src.shapes.point import Point
from src.shapes.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.center = Point(5.0, 5.0, (0, 0, 255))
        self.height = 2.0
        self.width = 4.0
        self.rectangle = Rectangle(self.center, self.width, self.height, (0, 0, 255))
        self.canvas = Canvas()

    def test_rectangle_draw(self):
        self.canvas.add_shape(self.rectangle)
        image = self.canvas.draw()
        self.assertTrue(np.any(image[3, 4] == [0, 0, 255]))
        self.assertTrue(np.any(image[7, 4] == [0, 0, 255]))
        self.assertTrue(np.any(image[3, 6] == [0, 0, 255]))
        self.assertTrue(np.any(image[7, 6] == [0, 0, 255]))

    def test_rectangle_translate(self):
        self.rectangle.translate(2.0, 3.0)
        self.assertEqual(self.rectangle.center.x, 7.0)
        self.assertEqual(self.rectangle.center.y, 8.0)

    def test_rectangle_scale(self):
        self.rectangle.scale(2)
        self.assertEqual(self.rectangle.width, 8.0)
        self.assertEqual(self.rectangle.height, 4.0)

if __name__ == '__main__':
    unittest.main()
