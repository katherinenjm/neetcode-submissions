class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def timeTaken(rate):
            hoursTaken = 0
            for i in piles:
                hoursperpile = -(-i//rate)
                hoursTaken += hoursperpile
            return hoursTaken 
         
        low = 1
        high = max(piles)
        lowest_yet = high


        while low <= high:
            mid = (low+high)//2
            
            if timeTaken(mid) -h > 0:
                low = mid +1
            else:
                
                lowest_yet = min(mid,lowest_yet)
                high = mid - 1
                print(f"for rate = {mid}, timeTaken = {timeTaken(mid)}, lowest_yet = {lowest_yet}")


        return lowest_yet




        