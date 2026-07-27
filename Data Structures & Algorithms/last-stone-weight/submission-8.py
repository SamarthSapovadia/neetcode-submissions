class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heappush,heappop
        heap = []
        for ele in stones:
            heappush(heap,-ele)
        while True:
            if len(heap)==1:
                return -heap[0]
            ele1 = heappop(heap)
            ele2 = heappop(heap)
            diff = -ele1 + ele2
            heappush(heap,-diff)


        