#Prob - count duplicate pairs in a given array
# A[i] == A[j] where i != j and (i, j) = (j, i)

# Method 1
def count_duplicate_pairs(A):
    freq = {}
    count = 0
    for val in A:
        if val in freq:
            count += freq.get(val)
        freq[val] = freq.get(val, 0) + 1
    return count

# Method 2 = nC2 = n(n-1)/2
def count_duplicate_pairs_1(A):
    freq = {}
    count = 0
    for val in A:
        freq[val] = freq.get(val, 0) + 1
    for val in freq.values():
        count += val * (val - 1) // 2
    return count


print(count_duplicate_pairs_1([1,2,1,3,1,2,4,5,1,4]))
