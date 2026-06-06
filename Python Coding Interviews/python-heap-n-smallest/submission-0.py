import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    return heapq.nsmallest(1,arr)[0]


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    return heapq.nsmallest(4,arr)


def get_min_2_elements(arr: List[int]) -> List[int]:
    incr_2min = heapq.nsmallest(2,arr)
    reverse_2min_smallest = []
    for num in incr_2min:
        heapq.heappush(reverse_2min_smallest, -num)
    decr_2min_smallest = []
    while reverse_2min_smallest:
        decr_2min_smallest.append(-heapq.heappop(reverse_2min_smallest))

    return decr_2min_smallest


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

