# for the problem description and context, please read prepare-the-bunnies-escape.md

MAX_WIDTH = 20
MAX_HEIGHT = 20
MAX_SCORE  = MAX_WIDTH * MAX_HEIGHT

# a simple container for relevant maze state
class Maze:
    def __init__(self, map):
        self.map = map
        self.w, self.h = len(map), len(map[0])
        self.start = (0, 0)
        self.end = (self.w - 1, self.h - 1)
        self.scores = {self.start: 1}
        self.rev_scores = {self.end: 1}
        # add all the walls to a set for ease of access
        self.walls = set()
        for y in range(self.h):
            for x in range(self.w):
                if map[x][y] == 1:
                    self.walls.add((x, y))

# returns the cardinal neighbours of a given position
def neighbours(pos, w, h):
    x, y = pos[0], pos[1]
    res = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    res = [p for p in res if w > p[0] >= 0 and h > p[1] >= 0]
    return res

# the number of steps needed to finish the maze with the given wall removed
def score_with_wall_removed(maze, wall):
    neighbour_scores = [maze.scores[n] for n in neighbours(wall, maze.w, maze.h) if n in maze.scores]
    rev_neighbour_scores = [maze.rev_scores[n] for n in neighbours(wall, maze.w, maze.h) if n in maze.rev_scores]
    if (len(rev_neighbour_scores) > 0 and len(neighbour_scores) > 0): 
        return min(rev_neighbour_scores) + min(neighbour_scores) + 1
    return MAX_SCORE

# perform a breadth first flood fill incrementing the score at each step
def breadth_first_fill(maze, scores, origin):
    parents = [origin]
    children = []
    while len(parents) > 0:
        for pos in parents:
            for neighbour in neighbours(pos, maze.w, maze.h):
                if neighbour not in maze.walls and neighbour not in scores:
                    scores[neighbour] = scores[pos] + 1
                    children.append(neighbour)
        parents = children
        children = []

# my solution performs two breadth first flood fill searches, one from the start of the maze and one from the end, recording
# the number of steps (the 'score') for each. Then for each wall in the maze we sum the smallest available score from both
# of these flood filled paths and choose to break the wall with the smallest score.
def solution(map, calculate_path=False):
    
    # initilase a maze object
    maze = Maze(map)

    # breadth first search assigning a score for each step forward
    breadth_first_fill(maze, maze.scores, maze.start)
    # a reverse breadth first search assigning a score for each step from the finish
    breadth_first_fill(maze, maze.rev_scores, maze.end)

    # find the best wall to remove
    score = MAX_SCORE
    for wall in maze.walls:
        wall_score = score_with_wall_removed(maze, wall)
        if wall_score < score:
            score = wall_score
            wall_to_remove = wall
    
    # if we want to caculate the actual path and not just the number of steps
    if calculate_path:
        # remove the wall
        maze.walls.remove(wall_to_remove)
        maze.map[wall_to_remove[0]][wall_to_remove[1]] = 0

        # find the shortest path with the wall now removed
        maze.scores = {start: 1}
        breadth_first_fill(maze, maze.scores, maze.start)

    return score

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
print("--- my test cases ---")
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [1, 0, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0],]))
print(solution([[0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0],]))

