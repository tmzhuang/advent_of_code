import sys
import logging
from day12.utils import *


def main():
    logging.basicConfig(
        # level=logging.INFO,
        level=logging.DEBUG,
        format='%(message)s',
        handlers=[logging.StreamHandler(sys.stdout)])
    logger = logging.getLogger()

    position = get_position('input1.txt')
    position, velocity = run_simulation(position, steps=None, capture_state=True)

if __name__ == '__main__':
    main()
