# Problem Description
# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
# If the given array contains a sub-array with sum zero return 1, else return 0.

def solve(arr):
    curr_sum = 0
    s = set()
    for val in arr:
        curr_sum += val

        if curr_sum == 0 or curr_sum in s:
            return 1
        s.add(curr_sum)
    return 0

print(solve([1, 2, 3, -5, 6]))