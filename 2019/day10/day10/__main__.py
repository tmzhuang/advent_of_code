import sys
import logging
from day10.utils import *
def main():
    logging.basicConfig(
        # level=logging.DEBUG,
        level=logging.INFO,
        format='%(message)s',
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    logger = logging.getLogger()

    a = get_array('input.txt')
    # a = get_array('input.txt')
    asteroids = get_asteroids(a)
    count, asteroid, vectors, reduced, unique = best_asteroid(asteroids)
    # print(count)
    print(f'Base is situated on {asteroid}.')
    sorted_asteroids = order_asteroids(asteroid, vectors, reduced, unique)
    print(f'200th asteroid: {sorted_asteroids[199]}')


if __name__ == '__main__':
    main()
