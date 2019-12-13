import re
import logging

import numpy as np


logger = logging.getLogger()
LINE_REGEX = r'^\s*<x=(?P<x>[-]?\d+),\s*y=(?P<y>[-]?\d+),\s*z=(?P<z>[-]?\d+)>\s*$'


def advance(position, velocity, return_diff=False):
    diff = np.empty_like(velocity)
    for i in range(position.shape[0]):
        p = position[i]
        others = np.delete(position, i, axis=0)
        add = np.less(p, others).sum(axis=0)
        sub = np.greater(p, others).sum(axis=0)
        diff[i] = add - sub
    # logger.debug(f'{diff=}')
    velocity += diff
    position += velocity
    result = [position, velocity]
    if return_diff:
        result.append(diff)
    return result


def run_simulation(position, velocity=None, steps=1, return_period=True, return_history=False):
    if not velocity:
        velocity = np.zeros(position.shape, dtype=int)
    if return_period:
        init = get_state(position, velocity)
        period = np.zeros(len(init), dtype=int)
    i = 1
    positions = [position.copy()]
    velocities = [velocity.copy()]
    # diffs = []
    while True:
        if steps and (i > steps):
            break
        # logger.debug(f'{i=}')
        # position, velocity, diff = advance(position, velocity, return_diff=True)
        position, velocity = advance(position, velocity)
        positions.append(position.copy())
        velocities.append(velocity.copy())
        # logger.debug(f'{velocities=}')
        # diffs.append(diff)
        if return_period:
            state = get_state(position, velocity)
            for j in range(len(state)):
                if not period[j] and (init[j] == state[j]):
                    period[j] = i
            if np.all(period):
                return np.lcm.reduce(period)
        # logger.debug(f'{position=}')
        # logger.debug(f'{velocity=}\n\n')
        i += 1
    result = [position, velocity]
    if return_history:
        result.append((np.array(positions), np.array(velocities)))
    return result


def calc_energy(position, velocity):
    p = np.abs(position).sum(axis=1)
    v = np.abs(velocity).sum(axis=1)
    return np.dot(p,v)


def get_position(filename):
    position = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            m = re.match(LINE_REGEX, line)
            position.append(np.array([int(m['x']), int(m['y']), int(m['z'])]))
    return np.array(position)


def get_state(position, velocity):
    return (position[:,0].tobytes() + velocity[:,0].tobytes(),
            position[:,1].tobytes() + velocity[:,1].tobytes(),
            position[:,2].tobytes() + velocity[:,2].tobytes())
