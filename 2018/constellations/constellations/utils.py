def str_to_pts(pts_str):
    ''' Converts a string representation of a list of points to a list of points,
    where a point is a list of integers.'''
    return [list(map(int, pt_str.strip().split(',')))
            for pt_str in pts_str.strip().split('\n')]

def is_in(constellation, p):
    ''' Returns true if p is in constellation, and false otherwise'''
    for p2 in constellation:
        current_mdist = mdist(p, p2)
        if current_mdist <= 3:
            return True
    return False

def dist(pair):
    ''' Calculates the absolute difference two values given as a list, pair
    eg. pair = [4,5]
    dist(pair) -> abs(4-5) -> 1
    '''
    return abs(pair[0] - pair[1])

def mdist(p1, p2):
    ''' Calculates the manhattan distance between points p1 and p2,
    where points are a list of integers.
    eg. p1 = [1,2,3,4]
    p2 = [2,3,6,1]
    mdist(p1, p2) -> 1 + 1 + 3 + 3 -> 8
    '''
    return sum(map(dist, zip(p1, p2)))

def calc_constellations(pts_str):
    pts = str_to_pts(pts_str)
    constellations = []
    for p in pts:
        adjacent_constellations = []
        rest = []
        for c in constellations:
            if is_in(c, p):
                adjacent_constellations.append(c)
            else:
                rest.append(c)
        if adjacent_constellations:
            # merge adjacent_constellations
            merged = reduce(operator.add, adjacent_constellations)
            # add current point to merged constellation
            merged.append(p)
            constellations = [merged, *rest]
        else:
            # create new constellation
            constellations.append([p])
    return len(constellations)

