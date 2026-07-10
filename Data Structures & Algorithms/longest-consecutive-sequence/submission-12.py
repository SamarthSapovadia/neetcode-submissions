class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        temp = 0
        max_ = -999
        if len(nums)==0:
            return temp
        for pos in range(len(nums)-1):
            if nums[pos]==nums[pos+1]:
                continue
            elif (nums[pos]-nums[pos+1]==-1) and (nums[pos+1]-nums[pos]==1) :
                print('yes')
                print(nums[pos],nums[pos+1])
                temp+=1
            else:
                print('No')
                print(temp,max_)
                print(nums[pos],nums[pos+1])
                if max_ <= temp:
                    max_ = temp+1
                    print(max_)
                temp = 0
        return max_ if max_ >temp else temp+1