# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float('-inf')
        def maxSoFar(root: TreeNode) -> int:
            nonlocal max_path
            if not root:
                return 0
            
            leftMax = maxSoFar(root.left)
            rightMax = maxSoFar(root.right)
            
            ret = max(root.val, max(root.val + leftMax, root.val + rightMax))
            max_path = max(max_path, leftMax + root.val + rightMax)
            
            if ret > 0:
                return ret
            else: 
                return 0
            
        maxSoFar(root)
        return max_path