# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        if not root:
            return 0
        self.P={0:1}
        self.ans=0
        self.dfs(root,target,root.val)
        return self.ans
    
    def dfs(self, root, t, val):
        self.ans += self.P.get(val-t,0)
        self.P[val] = self.P.get(val,0) + 1
        
        if root.left:
            self.dfs(root.left,t,val+root.left.val)
        if root.right:
            self.dfs(root.right,t,val+root.right.val)
        # remove the fact that this value appeared this many times because
        # we are moving to another branch. 
        self.P[val]-=1
        