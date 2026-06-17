class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth_largest_minheap = nums
        heapq.heapify(kth_largest_minheap)

        while len(kth_largest_minheap) > k:
            heapq.heappop(kth_largest_minheap)
        return kth_largest_minheap[0]         