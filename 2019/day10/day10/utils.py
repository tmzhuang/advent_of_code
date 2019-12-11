from collections import Counter
import numpy as np

ASTEROID = '#'
RIGHT = 0,1
UP = 1,0
LEFT = 0,-1
DOWN = -1,0


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
                    slopes.append(LEFT)
                elif v[0] > 0:
                    slopes.append(RIGHT)
                else:
                    #ignore zero vector
                    continue
            elif v[0] == 0:
                if v[1] < 0:
                    slopes.append(DOWN)
                elif v[1] > 0:
                    slopes.append(UP)
                else:
                    raise RuntimeError('Unreachable code.')
            else:
                slopes.append(reduce(v))
        slope_counts = Counter(slopes)
        los_counts[tuple(a)] = len(slope_counts)
    return los_counts


def max_los(los_counts):
    return max(los_counts.values())


def reduce(vector):
    while True:
        gcd = np.gcd.reduce(vector)
        if gcd == 1:
            return tuple(vector)
        else:
            vector = vector // gcd
