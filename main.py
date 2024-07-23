import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def linear_function(x, a, b):
    return a * x + b


points = [
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
    Point(4, 4),
    Point(5, 5),
    Point(6, 6),
    Point(7, 7),
    Point(8, 8),
    Point(9, 9),
    Point(10, 10)
]

x_values = np.array([point.x for point in points])
y_values = np.array([point.y for point in points])

parameters, parameters_covariance = curve_fit(linear_function, x_values, y_values)
print(parameters)

plt.plot(x_values, linear_function(x_values, parameters[0], parameters[1]))

plt.scatter(x_values, y_values, label="Points")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()