# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        que = deque()
        if root==None:
            return
        que.append(root)
        while que:
            node = que.pop()
            left  = node.left
            right = node.right
            if left:
                node.right = left
                que.append(left)
            else:
                node.right = None

            if right:
                node.left = right
                que.append(right)
            else:
                node.left = None

        return root
        