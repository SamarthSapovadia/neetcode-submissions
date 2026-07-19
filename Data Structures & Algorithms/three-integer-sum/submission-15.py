class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        two_sum_dict = defaultdict(list)
        dict_ = defaultdict()
        map_dict = defaultdict()
        pos = -1
        for ele in set(nums):
            pos = pos+1
            map_dict[ele] = pos
        arr = []

        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                two_sum = nums[i]+nums[j]
                two_sum_dict[two_sum].append([i,j])
        
        
        key_refresh = [0]*len(set(nums))
        for ele in range(0,len(nums)):
            if -nums[ele] in two_sum_dict:
                for val in two_sum_dict[-nums[ele]]:
                    key = key_refresh[:]
                    for ele_ in [nums[val[0]],nums[val[1]],nums[ele]]:
                        key[map_dict[ele_]]=1
                    if (ele in set(val)) or ((tuple(key) in dict_ )) :
                        pass
                    
                    else:
                        
                        dict_[tuple(key)]=1
                        arr.append([nums[ele],nums[val[0]],nums[val[1]]])
        return arr 




        