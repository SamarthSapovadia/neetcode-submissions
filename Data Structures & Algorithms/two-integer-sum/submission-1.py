class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        dict = defaultdict(list)
        for index in range(len(nums)):
            dict[nums[index]].append(index)
        for key ,value in dict.items():
            num = target-key
            if (num in dict):
                if (num ==key) and (len(dict[num])>1):
                    return dict[num]
                elif (num !=key):
                    print(key)
                    return [value[0],dict[num][0]]
