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
    common = dict()
    for i, s1 in enumerate(wire1):
        for j, s2 in enumerate(wire2):
            pt = intersect(s1, s2)
            # exclude (0,0) since we always start there
            if (pt is not None) and (not np.array_equal(pt, np.array([0,0]))):
                common[(i,j)] = pt
    return common


def closest_point(wire1, wire2, common):
    distances = [mdist(pt) for pt in common.values()]
    return np.minimum.reduce(distances)


def mdist(p1, p2=np.array([0,0])):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def calc_length(wire, index, p):
    '''
    Given point p which is on the segement at index in wire, returns the sum
    length of all previous segments in the wire plus the length of the start
    of the segement at index to point p
    '''
    length = 0
    for i in range(index+1):
        # segment given as vectors p + u
        p0, u = wire[i]
        if i != index:
            # point is not in p
            # euclidean distance of vector u
            length += np.linalg.norm(u)
        else:
            # point is in p
            length += np.linalg.norm(p-p0)
    return length


def calculate_shortest_move(wire1, wire2, common):
    pt_set = set()
    min_dist = None
    for k, p in common.items():
        # we only care about the first occurence of the intersect,
        # continue if we've seen it
        pt_tuple = tuple(p)
        if pt_tuple in pt_set:
            continue
        pt_set.add(pt_tuple)
        # i indicates index of segment in wire1 that the intersect occured
        # j indicates index of segment in wire2 that the intersect occured
        i,j = k
        # p is the point of intersection
        d1 = calc_length(wire1, i, p)
        d2 = calc_length(wire2, j, p)
        if not min_dist:
            min_dist = d1 + d2
        else:
            min_dist = min(min_dist, d1 + d2)
    return min_dist
