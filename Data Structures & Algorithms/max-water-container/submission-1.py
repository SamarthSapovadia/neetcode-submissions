class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights)-1
        max_area = -999
        while p2>p1:
            ele1 = heights[p1]
            ele2 = heights[p2]
            if ele1 >= ele2:
                area = ele2*(p2-p1)
                if area>max_area:
                    max_area = area
                p2 -=1
            if ele1 < ele2:
                area = ele1*(p2-p1)
                if area>max_area:
                    max_area = area
                p1 +=1
        return max_area
            

        