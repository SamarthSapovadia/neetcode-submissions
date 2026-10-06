class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from collections import deque
        subset = []
        que = deque()
        que.append(([],0))
        n = len(nums)
        while que:
            node,pos = que.popleft()
            if pos >= n:
                subset.append(node[:])
                continue
            node.append(nums[pos])
            que.append((node[:],pos+1))
            node.pop()
            que.append((node[:],pos+1))
        return subset


