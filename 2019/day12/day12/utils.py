import numpy as np

def advance(position, velocity):
    diff = np.empty_like(velocity)
    for i in range(position.shape[0]):
        p = position[1]
        others = np.delete(position, i, axis=0)
        add = np.greater(p, others).sum(axis=1)
        sub = np.less(p, others).sum(axis=1)
        diff[i] = add - sub
    velocity += diff
    position += velocity
    return position, velocity

def run_simulation(position, velocity=None, steps=1):
    if not velocity:
        velocity = np.zeros(position.shape)

    print(f'{position=}')
    print(f'{velocity=}')

    for i in range(steps):
