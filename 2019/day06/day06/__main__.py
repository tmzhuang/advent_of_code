from day06.utils import *


def main():
    nodes, parents = parse_tree_str()
    print(count_orbits(nodes, ROOT, 0))
    print(calc_orbital_change(parents))

if __name__ == '__main__':
    main()
