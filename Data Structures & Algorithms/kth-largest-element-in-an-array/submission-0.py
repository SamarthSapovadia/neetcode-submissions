class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush,heappop
        heap = []
        for ele in nums:
            if len(heap)<k:
                heappush(heap,ele)
            else:
                heappush(heap,ele)
                heappop(heap)

        return heappop(heap)

        