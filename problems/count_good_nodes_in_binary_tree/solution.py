# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root, m):
            if root: 
                m = max(root.val, m)
                if root.val >= m:
                    self.ans += 1
                dfs(root.left, m)
                dfs(root.right, m)
        dfs(root, root.val)
        return self.ans


            
"""         
Start time: 1:15AM
a) Binary tree search
"""