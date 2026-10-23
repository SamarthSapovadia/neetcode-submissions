class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import deque
        que = deque()
        combinatios = set()
        candidates.sort()
        que.append(([],0,0))
        n = len(candidates)
        set_check = set()
        while que:
            node,index,sum_ = que.popleft()
            
            if sum_==target:
                combinatios.add(tuple(node[:]))
                continue
            if (index >=n) or (sum_> target):
                continue
            node.append(candidates[index])
            if tuple(node) not in set_check:
                que.append((node[:],index+1,sum_+candidates[index]))
                set_check.add(tuple(node[:]))

            node.pop()
            que.append((node[:],index+1,sum_))
        final = []
        for ele in combinatios:
            final.append(list(ele))
        return final





        