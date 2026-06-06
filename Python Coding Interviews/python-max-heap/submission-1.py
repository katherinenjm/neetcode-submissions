import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    descend_list = []
    heapq.heapify(nums)
    for num in nums:
        heapq.heappush(max_heap, -num) # insert into heap_heap empty heap the neg of num
    while max_heap:
        descend_list.append(-heapq.heappop(max_heap))
    return descend_list








# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
