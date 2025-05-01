import unittest
from shapes import Triangle, Circle

class TestShapes(unittest.TestCase):

    def test_triangle_init(self):
        # Тестирование правильного инициализации треугольника
        triangle = Triangle([3, 4, 5])
        self.assertEqual(triangle.figure_sides, [3, 4, 5])
        self.assertTrue(triangle.is_right_angled)
        self.assertAlmostEqual(triangle.area, 6.0)

    def test_triangle_incorrect_sides(self):
        # Проверяем обработку неверных входных данных
        with self.assertRaises(ValueError):
            Triangle([-1, 2, 3])
        with self.assertRaises(ValueError):
            Triangle([1, 2, 4])
        with self.assertRaises(ValueError):
            Triangle([1, 2, 3, 5])
        with self.assertRaises(TypeError):
            Triangle(['string', 2, 3])

    def test_triangle_update_sides(self):
        # Тестирование изменения сторон и обновления свойств
        triangle = Triangle([3, 4, 5])
        triangle.figure_sides = [5, 12, 13]
        self.assertTrue(triangle.is_right_angled)
        self.assertAlmostEqual(triangle.area, 30.0)

    def test_circle_init(self):
        # Тестирование правильной инициализации круга
        circle = Circle(5)
        self.assertAlmostEqual(circle.area, 78.53981633974483)

    def test_circle_incorrect_radius(self):
        # Проверка обработки неправильного радиуса
        with self.assertRaises(ValueError):
            Circle(-1)
        with self.assertRaises(TypeError):
            Circle('not_a_number')


if __name__ == '__main__':
    unittest.main()
