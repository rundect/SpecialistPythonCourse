from __future__ import annotations

from typing import Tuple


class Point:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point: Point) -> float:
        return (((self.x - other_point.x) ** 2) + ((self.y - other_point.y) ** 2)) ** 0.5


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три, но порядок точек в списке и значение координат произвольные
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]


# Все точки одного цвета соединены линиями и образуют треугольник

# TODO-1: доработайте конструктор class Point для хранения цвета точки
# TODO-2: реализуйте метод dist_to(), для расчета расстояния между точками
# TODO-3: вычислите площади треугольников образованных точками разных цветов

def triangle_area(list_points: list) -> float:
    a, b, c = list_points
    # Формула Герона
    p = (a + b + c) / 2
    s = (p ** (p - a) ** (p - b) ** (p - c)) ** 0.5
    return s


def separate_points_by_colors(point: Point) -> list:
    if former_point is None:
        former_point = point
    else:
        distance = point.dist_to(former_point)
        triangle_area.append(distance)
        former_point = point
    return former_point


red_triangle_area = []
green_triangle_area = []
red_point = None
green_point = None

for point in points:
    if point.color == "red":
        red_point = separate_points_by_colors(point)
    else:
        green_point = separate_points_by_colors(point)
print("Площадь красного треугольника = ", ...)
print("Площадь зеленого треугольника = ", ...)
