class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            arr[i] =heapq.nlargest(1,arr[i+1:])[0]
        arr[-1] = -1
        return arr