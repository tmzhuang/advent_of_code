import logging
from collections import deque

import numpy as np

logger = logging.getLogger()

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
                (len(counts) > best_count)):
            best_count = len(counts)
            best_asteroid = a
            best_vectors = vectors
            best_reduced = reduced
            best_unique = unique
    return best_count, best_asteroid, best_vectors, best_reduced, best_unique


def reduce(vector):
    while True:
        gcd = np.gcd.reduce(vector)
        if gcd == 1:
            return vector
        else:
            vector = vector // gcd


def order_asteroids(asteroid, vectors, reduced, unique, max_iterations=None):
    if not max_iterations:
        max_iterations = vectors.shape[0]
    sorted_vectors = np.empty_like(vectors)
    radians = np.arctan2(unique[:,1], unique[:,0])
    # sorted indices of unique by radians
    indices = np.flip(np.argsort(radians))

    reduced_to_asteroid_mapping = {}
    for index in indices:
        vector = unique[index]
        mask = (reduced[:,0] == vector[0]) & (reduced[:,1] == vector[1])
        asteroid_indices = np.argwhere(mask).flatten()
        asteroids_in_line = vectors[asteroid_indices]
        distances = np.linalg.norm(asteroids_in_line, axis=1)
        sorted_distance_i = np.argsort(distances)
        sorted_asteroids_in_line = asteroids_in_line[sorted_distance_i]
        # reduced_to_asteroid_mapping[tuple(vector)] = deque(sorted_asteroids_in_line)
        d = deque(sorted_asteroids_in_line)
        reduced_to_asteroid_mapping[tuple(vector)] = d

    index_index = 0
    current_index = indices[index_index]
    for i in range(min(vectors.shape[0], max_iterations)):
        logger.debug(f'Looking for asteroid {i+1}.')
        got_asteroids = False
        vector = unique[current_index]
        angle = np.arctan2(vector[1], vector[0])
        logger.debug(f'{index_index=}')
        logger.debug(f'{current_index=}')
        logger.debug(f'{vector=}')
        logger.debug(f'{angle=}')
        asteroids_on_vector = reduced_to_asteroid_mapping[tuple(vector)]
        logger.debug(f'Asteroids in los: {asteroids_on_vector + asteroid}')
        asteroid_to_destroy = asteroids_on_vector.popleft()
        sorted_vectors[i] = asteroid_to_destroy
        logger.debug(f'ZAP! {asteroid_to_destroy + asteroid} incinerated.')
        logger.debug('')
        if len(asteroids_on_vector) == 0:
            logger.debug('Deleted an index')
            indices = np.delete(indices, index_index)
        else:
            index_index += 1
        if index_index >= indices.shape[0]:
            index_index = 0
        try:
            current_index = indices[index_index]
        except:
            pass
    return sorted_vectors + asteroid
