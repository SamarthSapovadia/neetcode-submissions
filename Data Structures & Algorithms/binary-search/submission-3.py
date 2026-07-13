class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums)-1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        

        while p2>p1:
            mid = (p2+p1)//2
            print(mid)
            if target > nums[mid]:
                p1 = mid+1
                if nums[p1]==target:
                    return p1
            elif target < nums[mid]:
                p2 = mid-1
                if nums[p2]==target:
                    return p2
            if nums[mid]==target:
                return mid
        return -1
        