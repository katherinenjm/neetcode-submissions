import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:

    heapq.heapify(strings)
    min_prior_heap = []
    #while strings:
    #    min_prior_heap.append(heapq.heappop(strings))
    #return min_prior_heap
    return strings



def heapify_integers(integers: List[int]) -> List[int]:
    heapq.heapify(integers)
    return integers


def heap_sort(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    ordered_nums= []
    while nums:
        ordered_nums.append(heapq.heappop(nums))
    return ordered_nums




# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
