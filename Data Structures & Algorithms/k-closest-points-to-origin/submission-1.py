class Solution:
    import math
    def eucledian_distanc(self,p1,p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heappush,heappop
        heap = []
        origin = [0,0]
        for ele in points:
            dist = self.eucledian_distanc(origin,ele)
            
            if len(heap)<k:
                heappush(heap,(-dist,ele))
            else:
                heappush(heap,(-dist,ele))
                heappop(heap)
        lst = []
        for dist,ele in heap:
            lst.append(ele)
        return lst



        