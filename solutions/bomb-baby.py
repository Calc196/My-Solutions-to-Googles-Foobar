# for the problem description and context, please read bomb-baby.md

# takes two numbers and returns the quotient and the remainder folowing an integer style division operation
def divide(bigger, smaller):
    quotient = bigger // smaller
    rem = bigger % smaller
    return quotient, rem


# returns the minimum number of steps needed to get from 1, 1 to m, f by adding one number to the other or vis a versa
def solution(m, f):
    lm, lf = long(m), long(f)
    n = 0L
    while (lm != 1L and lf != 1L):
        # we can increment n by the quotient and assign the larger of the two (mach or facula) to the remainder
        # this achieves the same effect as consecutive subtratctions (incrementing n by one each time) but is much faster
        if lm > lf:
            quotient, rem = divide(lm, lf)
            lm = rem
        else:
            quotient, rem = divide(lf, lm)
            lf = rem
        # if the remainder is 0, there is no solution
        if rem == 0: return "impossible"
        
        n += quotient
    
    return str(n + max(lm, lf) - 1)

print(solution("4", "7"))
print(solution("2", "1"))