# for the problem description and context, please read dodge-the-lasers.md

# the formula for the Beatty sequence of the square root of two was taken from here:
# http://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
# the formula is: S(n)=nn'(n+1)/2-n'(n'+1)/2-S(n') where n' = floor((sqrt(2) - 1)n)
# sometimes I feel like I'm just doing what the mathematicians tell me
# see also: https://en.wikipedia.org/wiki/Beatty_sequence

# the fractional part of the square root of 2 to 100 digits
ROOT_TWO_FRACTIONAL = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

# a recursive function that sums the Beatty sequence of sqrt(2) up to n
def s(n):
    # we end the recursion when n <= 1
    if n <= 1L:
        return long(n == 1L)
    # have to use integer division rather than python's math.floor() as python's floating point precision isn't sufficient
    n_dash = (ROOT_TWO_FRACTIONAL * n) // (10**100)
    return n * n_dash + n * (n + 1L) // 2L - n_dash * (n_dash + 1L) // 2L - s(n_dash)

def solution(str_n):
    n = long(str_n)
    return str(s(n))

print(solution("5"))
print(solution("77"))