# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict,deque
        level_dict = defaultdict(list)
        que = deque()
        if root is not None:
            que.append((root,0))
        while que:
            node,level = que.popleft()
            level_dict[level].append(node.val)
            if node.left:
                que.append((node.left,level+1))
            if node.right:
                que.append((node.right,level+1))
        arr = []
        for values in level_dict.values():
            arr.append(values)
        return arr
            

        