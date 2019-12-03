import numpy as np

def get_points(move_str, wire=None):
    moves = move_str.split(',')
    for move in moves:
        wire = attach(move, wire)
    return wire


def attach(move, wire=None):
    '''
    eg. append_points([(0,0)], 'R3') -> [(0,0),(0,1),(0,2),(0,3)]
    '''
    if wire is None:
        wire =[(0,0)]
    dir_ = move[0]
    units = int(move[1:])
    current = wire[-1]
    x,y = current
    if dir_ == 'R':
        new = [(z,y) for z in range(x+1, x+units+1)]
    elif dir_ == 'L':
        new = [(z,y) for z in range(x-1, x-units-1, -1)]
    elif dir_ == 'U':
        new = [(x,z) for z in range(y+1, y+units+1)]
    elif dir_ == 'D':
        new = [(x,z) for z in range(y-1, y-units-1, -1)]
    else:
        raise ValueError(f'Invalid move {move}.')
    return wire + new


def intersects(*wires):
    if len(wires) < 2:
        raise ValueError(f'Function requires at least 2 arguments, but {len(wires)} were found.')
    intersects = set(wires[0])
    for wire in wires[1:]:
        wire = set(wire)
        intersects &= wire
    return intersects


def closes_point(*move_strs):
    wires = [get_points(move_str)[1:] for move_str in move_strs]
    common = intersects(*wires)
    distances = [mdist(pt) for pt in common]
    return np.minimum.reduce(distances)


def mdist(p1, p2=(0,0)):
    a,b = p1
    c,d = p2
    return abs(a-c) + abs(b-d)


def calculate_shortest_moves(*move_strs):

