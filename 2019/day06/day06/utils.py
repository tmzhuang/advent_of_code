from collections import defaultdict


ROOT = 'COM'
YOU = 'YOU'
SAN = 'SAN'


def parse_tree_str(input_filename='input.txt'):
    nodes = defaultdict(list)
    parents = {}
    with open(input_filename, 'r') as f:
        for edge_str in f.readlines():
            parent, child = edge_str.rstrip().split(')')
            nodes[parent].append(child)
            parents[child] = parent
    return nodes, parents

def count_orbits(nodes, node_name, level):
    children = nodes[node_name]
    if not children:
        return level
    else:
        orbits = level
        for child in children:
            orbits += count_orbits(nodes, child, level+1)
    return orbits

def path_to_node(parents, node_name, stop_name=ROOT):
    path = []
    path.append(node_name)
    while node_name != stop_name:
        node_name = parents[node_name]
        path.append(node_name)
    if path:
        path.reverse()
    return path

def calc_orbital_change(parents, node1=YOU, node2=SAN):
    path1 = path_to_node(parents, node1)
    path2 = path_to_node(parents, node2)
    common_length = furthest_common_index(path1, path2) + 1
    # Don't include endpoints in count: -1 for YOU -1 for SAN
    return (len(path1) + len(path2) - common_length*2 - 2)


def furthest_common_index(path1, path2):
    lens = map(len, [path1, path2])
    min_len = min(lens)
    for i in range(min_len):
        if path1[i] != path2[i]:
            return i-1
    return min_len -1
