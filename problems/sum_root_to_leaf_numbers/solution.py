# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, value):
        if root:
            #if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.left, value*10+root.val)
            #if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.right, value*10+root.val)
            if not root.left and not root.right:
                self.res += value*10 + root.val