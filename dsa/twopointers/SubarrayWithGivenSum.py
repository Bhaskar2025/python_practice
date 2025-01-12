#Given an array of positive integers A and an integer B,
# find and return first continuous subarray which adds to B.
#If the answer does not exist return an array with a single integer "-1".

def subarray_with_given_sum(arr, target_sum):
    s = 0
    e = 0
    curr = 0
    for i in range(len(arr)):
        curr += arr[i]
        if curr >= target_sum:
            e = i

            while curr > target_sum and s < e:
                curr -= arr[s]
                s += 1
            if curr == target_sum:
                return arr[s:e + 1]

    return [-1]

print(subarray_with_given_sum([1, 2, 3, 4, 5], 5))