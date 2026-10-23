class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from collections import deque
        
        que = deque()
        n = len(nums) 
        que.append(([],[False]*n))
        permutation = []
        while que:
            node,poss = que.popleft()
            if len(node)== n:
                permutation.append(node[:])
                continue
            for i in range(n):
                if poss[i]==False:
                    node.append(nums[i])
                    poss[i] = True
                    que.append((node[:],poss[:]))
                    node.pop()
                    poss[i] = False
        return permutation