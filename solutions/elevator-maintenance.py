# for the problem description and context, please read elevator-maintenance.md

MAJOR_POS = 0
MINOR_POS = 1
REVISION_POS = 2
VERSION_DELIM = '.'

# non stable early exit comparison function
def compare(a, b):
    a1 = a.split(VERSION_DELIM)
    b1 = b.split(VERSION_DELIM)
    # compare major numbers
    a_major = int(a1[MAJOR_POS])
    b_major = int(b1[MAJOR_POS])
    if a_major < b_major: return -1
    if a_major > b_major: return 1
    # if identical, compare minor numbers (if they have them)
    if len(a1) < MINOR_POS + 1: return -1
    if len(b1) < MINOR_POS + 1: return 1
    a_minor = int(a1[MINOR_POS])
    b_minor = int(b1[MINOR_POS])
    if a_minor < b_minor: return -1
    if a_minor > b_minor: return 1
    # if still identical, compare revision numbers (if they have them)
    if len(a1) < REVISION_POS + 1: return -1
    if len(b1) < REVISION_POS + 1: return 1
    a_revision = int(a1[REVISION_POS])
    b_revision = int(b1[REVISION_POS])
    if a_revision < b_revision: return -1
    if a_revision > b_revision: return 1
    # identical
    return 0
    
# returns the sorted list of l, where l is a list of version numbers
def solution(l):
    return sorted(l, cmp=compare)

        

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))