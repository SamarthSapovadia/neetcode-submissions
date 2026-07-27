class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heappush,heappop
        
        
        # while True:
        #     lst = []
        #     heap = []
        #     if len(stones)==1:
        #         return stones[0]
        #     for ele in range(len(stones)):
        #         if len(heap)<2:
        #             heappush(heap,stones[ele])
        #         else:
        #             heappush(heap,stones[ele])
        #             pop = heappop(heap)
        #             lst.append(pop)
        #     ele1 = heappop(heap)
        #     ele2 = heappop(heap)
        #     diff = ele2-ele1
        #     lst.append(diff)
        #     print(lst)
        #     stones = lst[:]

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


        