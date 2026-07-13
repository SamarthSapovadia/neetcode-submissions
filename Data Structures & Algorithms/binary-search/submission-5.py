class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums)-1
        # if len(nums)==1:
        #     if nums[0]==target:
        #         return 0
        #     else:
        #         return -1
        

        while p2>=p1:
            mid = (p2+p1)//2
            print(mid)
            if nums[mid]==target:
                return mid
            elif target > nums[mid]:
                p1 = mid+1
            elif target < nums[mid]:
                p2 = mid-1

        return -1
        