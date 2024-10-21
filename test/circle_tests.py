import unittest
import numpy as np
from src.canvas import Canvas
from src.shapes.circle import Circle
from src.shapes.point import Point

class CirclesTest(unittest.TestCase):
    def setUp(self):
        self.center = Point(5.0, 5.0, (0, 255, 0))
        self.circle = Circle(3.0, self.center, (0, 255, 0))
        self.canvas = Canvas()

    def test_circle_draw(self):
        self.canvas.add_shape(self.circle)
        image = self.canvas.draw()
        self.assertTrue(np.any(image[5, 5] == [0, 255, 0]))

    def test_circle_translate(self):
        self.circle.translate(2.0, 3.0)
        self.assertEqual(self.circle.center.x, 7.0)
        self.assertEqual(self.circle.center.y, 8.0)

    def test_circle_scale(self):
        self.circle.scale(2.0)
        self.assertEqual(self.circle.radius, 6.0)

if __name__ == '__main__':
    unittest.main()