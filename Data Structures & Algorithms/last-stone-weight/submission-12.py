class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heapify, heappush, heappop

        heap = [-i for i in stones]
        heapify(heap)
        print(heap)
        while heap:
            if len(heap)==1:
                return -heappop(heap)
            ele1 = heappop(heap)
            ele2 = heappop(heap)
            diff = ele2-ele1
            if diff>0:
                heappush(heap,-diff)
        return 0