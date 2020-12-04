# for the problem description and context, please read minion-labour-shifts.md

# returns a list of all the elements in 'data' that occur 'n' times or less
def solution(data, n):
    counts = {}
    for i in data:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    res = [x for x in data if counts[x] <= n]
    return res

print(solution([1, 2, 3], 0))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))