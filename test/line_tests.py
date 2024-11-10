import unittest
import numpy as np
from src.canvas import Canvas
from src.shapes.line import Line
from src.shapes.point import Point

class TestLine(unittest.TestCase):
    def setUp(self):
        self.start = Point(1.0, 1.0, (255, 0, 0))
        self.end = Point(4.0, 4.0, (255, 0, 0))
        self.line = Line(self.start, self.end, (255, 0, 0))
        self.canvas = Canvas()

    def test_line_draw(self):
        self.canvas.add_shape(self.line)
        image = self.canvas.draw()
        self.assertTrue(np.any(image[1, 1] == [255, 0, 0]))
        self.assertTrue(np.any(image[4, 4] == [255, 0, 0]))

    def test_line_translate(self):
        self.line.translate(2.0, 3.0)
        self.assertEqual(self.line.point1.x, 3.0)
        self.assertEqual(self.line.point1.y, 4.0)
        self.assertEqual(self.line.point2.x, 6.0)
        self.assertEqual(self.line.point2.y, 7.0)

    def test_line_scale(self):
        self.line.scale(0.5)
        self.assertEqual(self.line.point1.x, 1.75)
        self.assertEqual(self.line.point1.y, 1.75)
        self.assertEqual(self.line.point2.x, 3.25)
        self.assertEqual(self.line.point2.y, 3.25)

if __name__ == '__main__':
    unittest.main()