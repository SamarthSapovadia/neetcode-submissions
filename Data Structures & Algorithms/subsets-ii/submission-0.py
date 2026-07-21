class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        from collections import deque

        que = deque()
        que.append(([],0))
        subset = set()
        nums.sort()
        while que:
            node,dist = que.pop()
            if dist==len(nums):
                subset.add(tuple(node))
                continue
            node.append(nums[dist])
            que.append((node[:],dist+1))
            node.pop()
            que.append((node[:],dist+1))
        final = []
        for ele in subset:
            final.append(list(ele))
        return final


        