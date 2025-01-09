# Problem Description
# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
# If the given array contains a sub-array with sum zero return 1, else return 0.

def solve(A):
    sum = 0
    s = set()
    for val in A:
        sum += val

        if sum == 0 or sum in s:
            return 1
        s.add(sum)
    return 0

print(solve([1, 2, 3, -5, 6]))