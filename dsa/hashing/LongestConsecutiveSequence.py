#Given an unsorted integer array A of size N.
#Find the length of the longest set of consecutive elements from array A.

def longest_consecutive_sequence(A):
    values = set(A)
    max_count = 0
    for val in values:
        if (val - 1) in values:
            continue
        else:
            start = val
            count = 1
            while (start + 1) in values:
                count += 1
                start += 1
        max_count = max(max_count, count)

    return max_count

print(longest_consecutive_sequence([100, 4, 200, 1, 4, 30, 40, 5, 3, 2]))
