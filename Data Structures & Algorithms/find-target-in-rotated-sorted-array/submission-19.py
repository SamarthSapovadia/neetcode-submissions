class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid]> nums[high]:
                low = mid+1
            elif nums[mid] < nums[high]:
                high = mid

        if target == nums[high]:
            return high
        elif target > nums[high] and target > nums[len(nums)-1]:
            low = 0
            high = high-1
            while low <= high:
                mid = (low+high)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]< target:
                    low = mid+1
                elif nums[mid] > target:
                    high = mid-1
        else:
            
            low = high
            high = len(nums)-1
            
            while low <= high:
                
                mid = (low+high)//2
                print(low,high,mid)
                if nums[mid]==target:
                    return mid
                elif nums[mid]< target:
                    low = mid+1
                elif nums[mid] > target:
                    high = mid-1
        return -1


        

            