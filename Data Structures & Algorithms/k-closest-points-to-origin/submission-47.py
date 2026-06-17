import numpy
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        length_dict = defaultdict(list)
        for point in points:
            dist_squared = point[0]**2 + point[1]**2
            length = numpy.sqrt(dist_squared)
            length_dict[length].append(point)


        # print(length_dict)
        dist_list = list(length_dict.keys())
        dist_list.sort()
        # print(dist_list)
        kclosest = []

 
        for key in dist_list:
            kclosest.extend(length_dict[key])
            print(f"for key = {key}, length_dict[key] = {length_dict[key]}]")
            if len(kclosest) == k:
                return kclosest



        