#Given an one-dimensional integer array A of size N and an integer B.

#Count all distinct pairs with difference equal to B.

def count_pairs_with_given_difference(arr, target):
    count = 0
    values = []
    for i in range(len(arr)):
        val = (target + arr[i])
        arr = arr[0:i] + arr[i + 1:]

        if val in arr and val not in values:
            values.append(val)
            count += 1

    return count

print(count_pairs_with_given_difference([8, 12, 16, 4, 0, 20], 4))