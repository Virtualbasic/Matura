'''

import random


def is_inside_circle(x, y):
    return x**2 + y**2 <= 1


with open("dane/punkty.txt", "r") as file:
    points = [line.split() for line in file.readlines()]


points = [(float(x), float(y)) for x, y in points]


sample_sizes = [100, 5000, len(points)]

for sample_size in sample_sizes:
    points_inside_circle = sum(1 for _ in range(sample_size) if is_inside_circle(*random.choice(points)))
    pi_approximation = 4 * points_inside_circle / sample_size
    print(f"Przybliżenie π dla {sample_size} punktów: {pi_approximation:.4f}")
ignore this
'''