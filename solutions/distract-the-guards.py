# for the problem description and context, please read distract-the-guards.md

from fractions import Fraction

MAX_GUARDS = 100
MAX_EDGES = MAX_GUARDS * MAX_GUARDS

def is_power_of_two(n):
    return (n & (n-1) == 0) and n != 0

# returns the simplified ratio of (x, y)
def simplify(x, y):
    frac = Fraction(x, y)
    return (frac.numerator, frac.denominator)

# determines whether the two numbers create an infinte sequence
def is_infinite(a, b):
    # if either number is 0 the sequence is infinite
    if a == 0 or b == 0: return True
    a, b = simplify(a, b)
    # if the sum of the reduced numbers is not a power of 2, the sequence is infinite, otherwise its finite
    return not is_power_of_two(a + b)

def solution(banana_list):
    l = banana_list
    num_guards = len(l)
    # build a table representing the connections between the guards that will loop forever, 
    # i.e. the edges of a graph
    edges = [[None] * num_guards for i in range(num_guards)]
    for i in range(num_guards):
        for j in range(num_guards):
            edges[i][j] = is_infinite(l[i], l[j])
    
    n = 0
    while n < num_guards:
        # we score a vertex (guard) by the number of edges
        scores = [sum(edges[i]) for i in range(num_guards)]
        # we can now score an edge by summing the scores of its vertices
        # with this we can loop through all the edges and select the one with the smallest score
        smallest, match = MAX_EDGES, None
        for i in range(num_guards):
            for j in range(num_guards):
                if edges[i][j]:
                    edge_score = scores[i] + scores[j]
                    if edge_score < smallest:
                        smallest = edge_score
                        match = (i, j)

        # if we couldn't find a match we have exhausted all connections and are finished
        if match == None:
            break
        
        # if we did find a match remove it from our graph and increment n by two
        for k in range(num_guards):
            edges[match[0]][k], edges[k][match[0]] = False, False
            edges[match[1]][k], edges[k][match[1]] = False, False
        n += 2

    # return the number of guards - the number of matches
    return num_guards - n


print(solution([1, 1]))
print(solution([1, 7, 3, 21, 13, 19]))
