# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque
        que_p = deque()
        que_q = deque()
        if p is not None:
            que_p.append(p)
        if q is not  None:
            que_q.append(q)

        while len(que_q) >0 and len(que_p) >0:
            node_p = que_p.popleft()
            node_q = que_q.popleft()
            if node_p.val == node_q.val:
                pass
            else:
                return False
            if ((node_p.left is not None) and (node_q.left is None)) or ((node_p.left is None) and (node_q.left is not None)):
                return False
            elif node_p.left:
                if (node_p.left.val == node_q.left.val):
                    que_p.append(node_p.left)
                    que_q.append(node_q.left)
                else:
                    return False
            
            if ((node_p.right is not None) and (node_q.right is None)) or ((node_p.right is  None) and (node_q.right is not None)):
                return False
            elif node_p.right:
                if (node_p.right.val == node_q.right.val):
                    que_p.append(node_p.right)
                    que_q.append(node_q.right)
                else:
                    return False

        if len(que_q)==0 and len(que_p)==0:
            return True
        else:
            return False






        