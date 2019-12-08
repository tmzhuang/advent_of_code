import numpy as np
import matplotlib.pyplot as plt

def get_arr():
    with open('input.txt', 'r') as f:
        input_ = f.read()
    arr = np.array(list(input_))
    arr = arr.astype('int')
    dim = (6, 25)
    nlayers = int(arr.size / dim[0] / dim[1])
    return arr.reshape((nlayers, dim[0], dim[1]))

def part1():
    arr = get_arr()
    # Get smallest layer
    min_i = None
    min_counts = None
    for i in range(arr.shape[0]):
        layer = arr[i]
        unique, counts = np.unique(layer, return_counts=True)
        counts = dict(zip(unique, counts))
        if min_i is None:
            min_i = i
            min_counts = counts
        elif counts[0] < min_counts[0]:
            min_i = i
            min_counts = counts
    return min_counts[1] * min_counts[2]

def part2():
    arr = get_arr()
    image = None
    for i in range(arr.shape[0]):
        layer = arr[i]
        if image is None:
            image = layer
        else:
            mask = image == 2
            image[mask] = layer[mask]
    plt.imsave('answer2.png', image, cmap='Greys')
    return
