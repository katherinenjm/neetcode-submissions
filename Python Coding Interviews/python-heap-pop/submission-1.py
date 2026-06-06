import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    ''' prior_min_list = [0]*len(heap)
    #print(f"heap = {heap},len(heap)={len(heap)}")

    for i in range(len(heap)):
        prior_min_list[i] = heapq.heappop(heap)
        #print(f"prior_min_list at i = {i} is {prior_min_list}")
    return prior_min_list
 '''
    priority = []
    while heap:
        priority.append(heapq.heappop(heap))
    return priority


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
