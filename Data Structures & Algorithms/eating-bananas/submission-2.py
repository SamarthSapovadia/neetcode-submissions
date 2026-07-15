class Solution:
    import math
    def check(self,arr,k):
        total_time = 0
        for ele in arr:
            total_time += (math.ceil(ele/k))
        return total_time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_s = max(piles)
        min_s = 1
        while max_s>=min_s:
            mid = (max_s+min_s)//2
            time = self.check(piles,mid)
            print(mid,max_s,min_s,time)
            if time <=h:
                max_s = mid-1
            elif time >h:
                min_s = mid+1
        return max_s+1