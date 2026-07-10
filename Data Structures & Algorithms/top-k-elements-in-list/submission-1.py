class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dict_ = defaultdict(int)
        for ele in nums:
            dict_[ele]+=1
        keys = sorted(dict_.items(),key=lambda x:x[1])
        keys = [x for x,y in keys]
        print(keys)
        arr = []
        if len(dict_)<k:
            k = len(dict_)
        for i in range(1,k+1):
            arr.append(keys[-i])
        return arr



        