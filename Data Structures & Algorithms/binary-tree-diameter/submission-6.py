# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def left_right_height(self,node):
        from collections import deque
        left_que = deque()
        right_que = deque()
        max_left_height = 0
        max_right_height = 0
        if node.left:
            left_que.append((node.left,1))
        if node.right:
            right_que.append((node.right,1))
        while left_que:
            node,depth = left_que.pop()
            if depth > max_left_height:
                max_left_height = depth
            if node.left:
                left_que.append((node.left,depth+1))
            if node.right:
                left_que.append((node.right,depth+1))
    
        while right_que:
            node,depth = right_que.pop()
            if depth > max_right_height:
                max_right_height = depth
            if node.left:
                right_que.append((node.left,depth+1))
            if node.right:
                right_que.append((node.right,depth+1))
        return max_left_height,max_right_height


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        que = deque()
        que.append(root)
        while que:
            node = que.pop()
            left_height,right_height = self.left_right_height(node)
            if left_height+right_height > max_diameter:
                max_diameter = left_height+right_height
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return max_diameter
        