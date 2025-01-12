#Given a sorted array of integers (not necessarily distinct) A and an integer B,
# find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.

def count_pairs_with_sum_k(arr, k):
    freq = {}
    count = 0
    for value in arr:
        if k - value in freq:
            count += freq[k - value]
        freq[value] = freq.get(value, 0) + 1
    return count % ((10 ** 9) + 7)

print(count_pairs_with_sum_k([1, 5, 7, 10], 8))