# for the problem description and context, please read bringing-a-gun-to-a-guard-fight.md

from math import sqrt
from fractions import Fraction

ORIGIN = (0,0)
UP, DOWN, RIGHT, LEFT = (0,1), (0,-1), (1,0), (-1,0)
DIAMOND_DIRECTIONS = [DOWN, RIGHT, LEFT, UP]

def magnitude(x, y):
    return sqrt(x * x + y * y)

# returns the simplified direction of (x, y).
# e.g: simplify(3, -6) -> (2, -3) and simplify(401, 0) -> (1, 0)
def simplify(x, y):
    if x == 0 or y == 0:
        return (int(x > 0), int(y > 0))
    signx = -1 if x < 0 else 1
    signy = -1 if y < 0 else 1
    frac = Fraction(abs(x), abs(y))
    return (signx * frac.numerator, signy * frac.denominator)

# given a position (x, y), we return the neighbouring positions so as to build the next layer of a diamond shape
def expand_diamond_cell(x, y):                                          # the diamond expansion shown to iteration 4:
    if ((x, y) == ORIGIN):                                              #         4        
        return DIAMOND_DIRECTIONS                                       #       4 3 4      
    idx = (x > 0) + (y > 0) * 2                                         #     4 3 2 3 4    
    d = DIAMOND_DIRECTIONS[idx]                                         #   4 3 2 1 2 3 4  
    expansions = [(x + d[0], y + d[1])]                                 # 4 3 2 1 0 1 2 3 4
    if x == 0 or y == 0:                                                #   4 3 2 1 2 3 4  
        d = DIAMOND_DIRECTIONS[idx + (x == 0) + 2 * (y == 0)]           #     4 3 2 3 4    
        expansions.append((x + d[0], y + d[1]))                         #       4 3 4      
    return expansions                                                   #         4        

# The key insight I had which allowed me to solve this problem is that the process of reflecting a ray 
# off a wall is equivalent to reflecting the room about the wall's axis and keeping the ray straight.
# by transforming the room rather than the ray itself we can expand spatially and iteratively, 
# considering all the possible transformed rooms (translated and reflected) within the ray's distance.
def solution(dimensions, your_position, guard_position, distance):
    w, h = dimensions[0] + 1, dimensions[1] + 1
    myx, myy = your_position[0], your_position[1]
    gx, gy = guard_position[0], guard_position[1]

    # directions in which we hit guards
    guard_dirs = {}
    # directions in which we hit ourself
    me_dirs = {}
    # parents is the list of nodes to consider, where a node represents a potentially reflected and 
    # translated version of the room that we and the guard are standing in. 
    parents = [ORIGIN]
    while len(parents) > 0:
        children = []
        for parent in parents:
            nx, ny = parent
            # we reflect the room about each axis depending on the parity of the coordinates (nx, ny)
            mirror_myx = myx if (nx % 2) == 0 else w - 1 - myx
            mirror_myy = myy if (ny % 2) == 0 else h - 1 - myy
            mirror_gx = gx if (nx % 2) == 0 else w - 1 - gx
            mirror_gy = gy if (ny % 2) == 0 else h - 1 - gy
            # we translate the room by (w, h) to reach the cordinates (nx, ny)
            mirror_myx = mirror_myx + w * nx
            mirror_myy = mirror_myy + h * ny
            mirror_gx = mirror_gx + w * nx
            mirror_gy = mirror_gy + h * ny
            # establish vectors from our real position to our transformed self and to the guard
            to_me_x = (mirror_myx - nx) - myx
            to_me_y = (mirror_myy - ny) - myy
            to_guard_x = (mirror_gx - nx) - myx
            to_guard_y = (mirror_gy - ny) - myy
            # magnitudes
            len_to_me = magnitude(to_me_x, to_me_y)
            len_to_guard = magnitude(to_guard_x, to_guard_y)

            # we do not consider any nodes further out than the max distance
            if len_to_guard > distance:
                continue
            # get the node's children as dictated by the next layer of our expanding diamond algorithm
            children += expand_diamond_cell(parent[0], parent[1])
            
            # simplify our direction vectors
            to_me = simplify(to_me_x, to_me_y)
            to_guard = simplify(to_guard_x, to_guard_y)
            # insert each direction into its correct dictionary. we first check that the given direction is 
            # not in either dictionary. We then ensure that if the two directions are equivalent, the vector 
            # with the smaller magnitude (i.e. the closer one) is inserted into the dictionary.
            if to_me not in me_dirs and to_me not in guard_dirs and (to_me != to_guard or len_to_me < len_to_guard):
                me_dirs[to_me] = len_to_me
            if to_guard not in guard_dirs and to_guard not in me_dirs and (to_guard != to_me or len_to_guard < len_to_me):
                guard_dirs[to_guard] = len_to_guard
        
        # the children amassed this iteration form the next layer of our search
        parents = children

    return len(guard_dirs)

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))
