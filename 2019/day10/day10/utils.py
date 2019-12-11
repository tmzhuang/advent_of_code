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


def best_asteroid(asteroids):
    los_counts = {}
    best_count = None
    for i in range(asteroids.shape[0]):
        a = asteroids[i]
        others = np.delete(asteroids, i, 0)
        vectors = others - a
        reduced = np.array([reduce(v) for v in vectors])
        unique, counts = np.unique(reduced, return_counts=True, axis=0)
        if ((best_count is None) or
                (len(counts) > best_count))  :
            best_count = len(counts)
            best_asteroid = a
            best_vectors = vectors
            best_reduced = reduced
    return best_count, best_asteroid, best_vectors, reduced


def reduce(vector):
    while True:
        gcd = np.gcd.reduce(vector)
        if gcd == 1:
            return vector
        else:
            vector = vector // gcd


def order_asteroids(asteroid, vectors, reduced):
    unique, i,j = np.unique(reduced, return_index=True, return_inverse=True, axis=0)
    breakpoint()

