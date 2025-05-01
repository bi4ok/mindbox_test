from shapes import Triangle, Circle

if __name__ == '__main__':
    triangle = Triangle([5, 12, 13])
    print(f"Треугольник со сторонами: {triangle.figure_sides}, "
          f"Его площадь: {triangle.area}, "
          f"Он {['не ', ''][triangle.is_right_angled]}прямоугольный")

    circle = Circle(5)
    print(f"Круг с радиусом: {circle.radius}, "
          f"Его площадь: {circle.area}, ")