class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heapify, heappush, heappop

        heap = [-ele for ele in stones]
        heapify(heap)   # O(n) instead of O(n log n)

        while len(heap) > 1:
            ele1 = heappop(heap)
            ele2 = heappop(heap)
            diff = -ele1 + ele2
            if diff != 0:
                heappush(heap, -diff)

        return -heap[0] if heap else 0

        