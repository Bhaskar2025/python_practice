# Find the minimum distance between any two duplicate elements in an array

def find_min_distance_between_duplicates(A):
    position_map = {}
    min_distance = len(A)

    for i in range(len(A)):
        if A[i] in position_map:
            min_distance = min(min_distance, i - position_map.get(A[i]))
        position_map[A[i]] = i

    return min_distance

print(find_min_distance_between_duplicates([1,2,7,3,1,2,4,5,1,4]))