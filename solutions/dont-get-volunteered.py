# for the problem description and context, please read dont-get-volunteered.md

NUM_ROWS = 8
NUM_COLUMNS = 8
CORNERS = [0, NUM_ROWS - 1, NUM_ROWS * NUM_COLUMNS - NUM_COLUMNS, NUM_ROWS * NUM_COLUMNS - 1]
def is_corner(pos):
    return pos in CORNERS

# A constant time solution for the number of moves it takes to move a knight from one position to another on a 
# standard chess board. While this problem can be solved by searching a graph, I wanted to see if I could find
# a constant time solution.
def solution(src, dest):
    # handle simplest case
    if (src == dest):
        return 0
    # extract positions
    src_row, src_column = src // NUM_ROWS, src % NUM_COLUMNS
    dest_row, dest_column = dest // NUM_ROWS, dest % NUM_COLUMNS
    # calculate deltas
    row_delta = abs(src_row - dest_row)
    column_delta = abs(src_column - dest_column)
    delta = (row_delta + column_delta)
    # determine number of moves
    # the number of the main distance covering moves
    main = delta // 3
    # the number of moves to reposition and align with the destination
    to_align = delta % 3
    n = main + to_align
    # are the src and dest exactly diagonal from one another
    diagonal = row_delta == column_delta
    # are the src and dest too similar along a given axis
    too_similar = (row_delta <= (main - 1 - to_align) or column_delta <= (main - 1 - to_align))
    # if positions are too similar we need to add two extra turns
    if to_align == 0 and too_similar: 
        n += 2
    # if positions are too similar or at imperfect diagonals (i.e. main % 3 != 0) or we're cramped for space (i.e.
    # main < 1), add two extra turns
    elif to_align == 1 and (too_similar or (diagonal and (main % 3) != 0) or main < 1): 
        n += 2
    # if positions are close together (i.e. main < 1) and at diagonals and either the src or dest is in the corner,
    # add two extra turns
    elif to_align == 2 and main < 1 and diagonal and (is_corner(src) or is_corner(dest)): 
        n += 2
    return n

print(solution(19, 36))
print(solution(0, 1))
