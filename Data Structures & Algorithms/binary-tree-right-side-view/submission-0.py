# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict,deque
        que = deque()
        if root ==None:
            return []
        que.append((root,0))
        dict_level = defaultdict(list)
        
        view = []
        print(que)
        while que:
            node,level = que.popleft()
            dict_level[level].append(node.val)
            if node.left:
                que.append((node.left,level+1))
            if node.right:
                que.append((node.right,level+1))
        for ke,values in dict_level.items():
            view.append(values[-1])
        return view



        