from itertools import product

import numpy as np

def get_wire(move_str):
    segments=[]
    moves = move_str.split(',')
    p0 = np.array([0,0])
    for move in moves:
        # parametrized segement -> p0 + s*u where s is a scalar [0,1] and u is a vector
        p0, u = get_segment(p0, move)
        segments.append((p0, u))
        p0 = p0 + u
    return segments


def get_segment(p0, move):
    '''
    eg. get_segement((0,2), 'R3') -> ((0,2), (3,0))
    '''
    dir_ = move[0]
    s = int(move[1:])
    if dir_ == 'R':
        u_hat = np.array([1,0])
    elif dir_ == 'L':
        u_hat = np.array([-1,0])
    elif dir_ == 'U':
        u_hat = np.array([0,1])
    elif dir_ == 'D':
        u_hat = np.array([0,-1])
    else:
        raise ValueError(f'Invalid move {move}.')
    return p0, s*u_hat


def intersect(s1, s2):
    # See http://geomalgorithms.com/a05-_intersect-1.html
    p0, u = s1
    q0, v = s2
    # Get a vector perpendicular to v
    v_p = np.array([v[1], -v[0]])
    denom = np.dot(u, v_p)
    if denom == 0:
        # lines are parallel or degenerate
        return None
    w = p0 - q0
    u_p = np.array([u[1], -u[0]])
    s_i = -np.dot(w,v_p)/denom
    t_i = -np.dot(w,u_p)/denom
    if (0<=s_i<=1) and (0<=t_i<=1):
        return p0 + s_i*u
    return None


def get_common_points(wire1, wire2):
    common = list()
    for s1, s2 in product(wire1, wire2):
        pt = intersect(s1, s2)
        if (pt is not None) and (not np.array_equal(pt, np.array([0,0]))):
            common.append(pt)
    return common


def closest_point(move_str1, move_str2):
    wire1 = get_wire(move_str1)
    wire2 = get_wire(move_str2)
    common = get_common_points(wire1, wire2)
    distances = [mdist(pt) for pt in common]
    return np.minimum.reduce(distances)


def mdist(p1, p2=np.array([0,0])):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def calc_dist(wire, pt):
    dist = 0
    for point in wire:
        if point == pt:
            return count
        count += 1
    raise ValueError(f'Point {pt} not found in wire {wire}.')

def point_is_in(segment, pt):
    p, u = segment
    s = (pt-p) / u


def calculate_shortest_move(*move_strs):
    wires = [get_points(move_str) for move_str in move_strs]
    common = intersects(*wires)
    dist = None
    for pt in common:
        wire_dist = 0
        for wire in wires:
            wire_dist += calc_dist(wire, pt)
        if not dist:
            dist = wire_dist
        else:
            dist = min(dist, wire_dist)
    return dist

