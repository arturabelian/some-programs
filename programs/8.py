# Нахождение площади треугольника по формуле Герона.

# s = (side_a + side_b + side_c) / 2
# sqrt(square * (square - side_a) * (square - side_b) * (square - side_c))

import math

def heron(side_a, side_b, side_c):
    square = (side_a + side_b + side_c) / 2
    return math.sqrt(square * (square - side_a) * (square - side_b) * (square - side_c))

print(heron(10, 10, 10))

# 43,3