from day06.utils import *


def main():
    nodes = parse_tree_str()
    breakpoint()
    print(count_orbits(nodes, ROOT, 0))

if __name__ == '__main__':
    main()
