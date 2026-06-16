class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #create maxheap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        print(max_heap)
        
        #strart smaching stones while lean(max_heap)>1
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap, -abs(x-y))

                # print(max_heap)
        if max_heap:
            return -max_heap[0]
        else:
            return 0
        



        
        

        