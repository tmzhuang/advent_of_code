import sys
import logging
from day12.utils import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    logging.basicConfig(
        # level=logging.INFO,
        level=logging.DEBUG,
        format='%(message)s',
        handlers=[logging.StreamHandler(sys.stdout)])
    logger = logging.getLogger()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    position = get_position('input1.txt')
    position, velocity, history = run_simulation(position, steps=2773, return_history=True)
    p,v = history
    for i in range(p.shape[1]):
        if i == 1:
            moon = p[:,i,:]
            # moon = v[:,i,:]
            ax.plot(xs=moon[:,0], ys=moon[:,1], zs=moon[:,2])
    fig.show()
    breakpoint()


if __name__ == '__main__':
    main()
