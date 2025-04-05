from typing import Callable
import numpy as np


def fixed_point_iteration(
    x: float, y: float, f: Callable[[float], float], g: Callable[[float], float], n: int
) -> tuple[float, float]:
    """
    Basic fixed-point iteration function

    x: staring point for x
    y: staring point for y
    f: function f(x)
    g: function g(y)
    n: number of iterations
    returns: tuple of x and y
    """

    if n == 0:
        return (x, y)

    return fixed_point_iteration(f(x), g(y), f, g, n - 1)


if __name__ == "__main__":
    start_x = 1
    start_y = -0.5

    def f(x):
        return np.sqrt(x)

    def g(x):
        return np.cos(x)

    x, y = fixed_point_iteration(start_x, start_y, f, g, 5)
    print(x, y)
