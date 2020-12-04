# for the problem description and context, please read fuel-injection-perfection.md

# this solution is O(k) where k is the number of times that consecutive bits of n differ, plus 1. 
# e.g. for 3855 (or in binary: 111100001111) k = 3
def solution(n):
    turns = 0
    num = long(n)
    while num != 1:
        # special case handling for binary strings which eventually reduce to 3
        if num == 3:
            turns += 2
            break
        
        # convert the number to a binary string
        bin_string = "{0:b}".format(num)
        # count the trailing zeroes - we allow the last bit to be either a 1 or a zero (notice the splice [:-1])
        trailing_zeroes = len(bin_string) - len(bin_string[:-1].rstrip('0'))
        # count the trailing ones
        trailing_ones = len(bin_string) - len(bin_string.rstrip('1'))
        
        # if there are mores trailing ones than zeroes, we should add one to get a nice run of zeroes
        add_one = trailing_ones > trailing_zeroes
        # otherwise we have more trailing zeroes and so we should subtract one if the last bit is set
        subtract_one = not add_one and (num & 1)
        # we divide by two for the longer run (of either ones or zeroes)
        divide_by_twos = max(trailing_ones, trailing_zeroes)

        num += add_one
        num -= subtract_one # not strictly neccessary
        num >>= divide_by_twos

        turns += add_one + subtract_one + divide_by_twos

    return turns

print(solution("15"))
print(solution("4"))
print("--- my test cases ---")
print(solution(str((1L << 1024) - 1)))
print(solution("153"))
print(solution("48"))