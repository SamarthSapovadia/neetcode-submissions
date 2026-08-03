# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def right_left_height(self,node):
        from collections import deque
        l_node = node.left
        r_node = node.right

        l_que = deque()
        r_que = deque()

        max_l_depth = 0
        max_r_depth = 0
        if l_node:
            l_que.append((l_node,1))
        if r_node:
            r_que.append((r_node,1))

        while l_que:
            node,dist = l_que.popleft()
            if dist > max_l_depth:
                max_l_depth = dist
            if node.left:
                l_que.append((node.left,dist+1))
            if node.right:
                l_que.append((node.right,dist+1))

        while r_que:
            node,dist = r_que.popleft()
            if dist > max_r_depth:
                max_r_depth = dist
            if node.left:
                r_que.append((node.left,dist+1))
            if node.right:
                r_que.append((node.right,dist+1))
        return abs(max_l_depth-max_r_depth)



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        que = deque()
        if root:
            que.append(root)
        while que:
            node = que.popleft()
            diff = self.right_left_height(node)
            if diff >1:
                return False
            if node.right:
                que.append(node.right)
            if node.left:
                que.append(node.left)
        return True

        