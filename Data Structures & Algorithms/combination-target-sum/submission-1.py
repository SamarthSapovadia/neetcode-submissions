class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import deque
        que = deque()
        que.append(([],0))
        subset = []
        n = len(nums)
        while que:
            node,dist = que.popleft()
            if sum(node)==target :
                subset.append(node)
                continue
            elif (sum(node)> target) or dist >= len(nums):
                continue
            node.append(nums[dist])
            que.append((node[:],dist))
            node.pop()
            que.append((node[:],dist+1))
        return subset
