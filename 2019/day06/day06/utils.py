from collections import defaultdict


ROOT = 'COM'


def parse_tree_str(input_filename='input.txt'):
    nodes = defaultdict(list)
    with open(input_filename, 'r') as f:
        for edge_str in f.readlines():
            edge = edge_str.split(')')
            c
            nodes[parent].append(child)
    return nodes

def count_orbits(nodes, node_name, level):
    children = nodes[node_name]
    if not children:
        return level
    else:
        orbits = level
        for child in children:
            orbits += count_orbits(nodes, child, level+1)
    return orbits

