class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import deque
        que = deque()
        que.append(([],0))
        subset = []
        n_ = len(nums)
        while que:
            node,pos = que.pop()
            if sum(node)==target:
                subset.append(node[:])
                continue
            elif sum(node)>target or pos >= n_:
                continue
            node.append(nums[pos])
            que.append((node[:],pos))
            node.pop()
            que.append((node[:],pos+1))
        return subset



        