# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from collections import deque
        que = deque()
        que.append(root)
        main_tree_node = []
        while que:
            node = que.popleft()
            if node.val == subRoot.val:
                main_tree_node.append(node)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        if main_tree_node:
            print(main_tree_node)
            for ele in main_tree_node:
                que_main = deque()
                que_sub = deque()
                que_main.append(ele)
                que_sub.append(subRoot)
                flag = True
                while que_main or que_sub:
                    node_main = que_main.popleft()
                    node_sub = que_sub.popleft()
                    if (node_main is None) or (node_sub is None) or (node_main.val != node_sub.val):
                        flag =  False
                        break
                    if node_main.left or node_sub.left:
                        que_main.append(node_main.left) if node_main.left is not None else que_main.append(None)
                        que_sub.append(node_sub.left) if node_sub.left is not None else que_sub.append(None)
                    if node_main.right or node_sub.right:
                        que_main.append(node_main.right) if node_main.right is not None else que_main.append(None)
                        que_sub.append(node_sub.right) if node_sub.right is not None else que_sub.append(None)
                    print(node_main.val,node_sub.val)

                if flag:
                    return True
            return False 

        else:
            return False
            
        