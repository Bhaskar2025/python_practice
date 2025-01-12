# Find the minimum distance between any two duplicate elements in an array

def find_min_distance_between_duplicates(arr):
    position_map = {}
    min_distance = len(arr)

    for i in range(len(arr)):
        if arr[i] in position_map:
            min_distance = min(min_distance, i - position_map.get(arr[i]))
        position_map[arr[i]] = i

    return min_distance

print(find_min_distance_between_duplicates([1,2,7,3,1,2,4,5,1,4]))