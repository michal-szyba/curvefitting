import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(2, 3)
print(point1.x, point1.y)
points = [
    Point(1, 2),
    Point(2, 3),
    Point(3, 4),
    Point(4, 5),
    Point(5, 6),
    Point(6, 7),
    Point(7, 8),
    Point(8, 9),
    Point(9, 10),
    Point(10, 11)
]

x_values = np.array([point.x for point in points])
y_values = np.array([point.y for point in points])

plt.scatter(x_values, y_values)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()