#Given N non-negative integers A[0], A[1], ..., A[N-1] ,
# where each represents a point at coordinate (i, A[i]).
# N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).
# Find two lines, which together with x-axis forms a container,
# such that the container contains the most water. You need to return this maximum area.

def container_with_most_water(arr):
    if len(arr) <= 1:
        return 0

    start = 0
    end = len(arr) - 1

    max_area = 0
    while start < end:
        max_area = max(max_area, min(arr[start], arr[end]) * (end - start))
        if arr[start] > arr[end]:
            end -= 1
        else:
            start += 1
    return max_area

print(container_with_most_water([1, 5, 4, 3]))