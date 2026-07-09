class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        dict = defaultdict(int)
        for ele in nums:
            dict[ele]+=1
            if dict[ele]>1:
                return True
        return False
        