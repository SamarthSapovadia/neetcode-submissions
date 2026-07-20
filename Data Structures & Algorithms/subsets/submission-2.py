class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from collections import deque
        que = deque()
        subset = []
        n = len(nums)
        que.append(([],0))
        while que:
            node,dist = que.popleft()
            if dist == n:
                subset.append(node[:])
                continue
            node.append(nums[dist])
            que.append((node[:],dist+1))
            node.pop()
            que.append((node[:],dist+1))
        return subset

            


        