from fractions import Fraction
from collections import Counter
import numpy as np

ASTEROID = '#'

def get_array(filename):
    width = None
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            rows.append(np.array(list(line)))
    return np.array(rows) == ASTEROID

def get_asteroids(arr):
    return np.argwhere(arr)

RIGHT_HORIZONTAL = 0
LEFT_HORIZONTAL = 1
UP_VERTICAL = 2
DOWN_VERTICAL = 3

def count_los(asteroids):
    los_counts = {}
    for i in range(asteroids.shape[0]):
        a = asteroids[i]
        others = np.delete(asteroids, i, 0)
        vectors = others - a
        slopes = []
        for v in vectors:
            if v[1] == 0:
                if v[0] < 0:
                    slopes.append(LEFT_HORIZONTAL)
                elif v[0] > 0:
                    slopes.append(RIGHT_HORIZONTAL)
                else:
                    #ignore zero vector
                    continue
            elif v[0] == 0:
                if v[1] < 0:
                    slopes.append(DOWN_VERTICAL)
                elif v[1] > 0:
                    slopes.append(UP_VERTICAL)
                else:
                    raise RuntimeError('Unreachable code.')
            else:
                slopes.append(Fraction(int(v[0]), int(v[1])))
        breakpoint()
        slope_counts = Counter(slopes)
        los_counts[tuple(a)] = len(slope_counts)
