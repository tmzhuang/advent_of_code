import sys
import logging
from day12.utils import *
def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        handlers=[logging.StreamHandler(sys.stdout)])
    logger = logging.getLogger()

if __name__ == '__main__':
    main()
