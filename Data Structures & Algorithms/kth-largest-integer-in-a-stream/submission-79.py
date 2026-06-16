
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap =nums
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)
        #leaves us with minheap[0] = kth largest





    def add(self, val: int) -> int:

        
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        print(self.minheap)
        
        return self.minheap[0]
        

        


