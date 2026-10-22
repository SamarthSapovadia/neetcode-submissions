class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import deque
        subset = []
        que = deque()
        que.append(([],0))
        while que:
            node,index = que.popleft()
            if index>=len(nums):
                continue
            if sum(node)==target:
                subset.append(node[:])
                continue
            if sum(node)>target:
                continue
            node.append(nums[index])
            que.append((node[:],index))
            node.pop()
            que.append((node[:],index+1))
        return subset
                   