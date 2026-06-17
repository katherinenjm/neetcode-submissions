import numpy
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_minheap = []

        for point in points:
            dist_sq = point[0]**2 + point[1]**2
            dist_minheap.append([dist_sq,point])
        heapq.heapify(dist_minheap)


        kclosest = []
        while k > 0:
            dist, point = heapq.heappop(dist_minheap)
            kclosest.append(point)
            k -= 1
        return kclosest

        