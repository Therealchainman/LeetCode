# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def dfs(root, count=0):
            if not root:
                return 0
            count ^= 1 << (root.val - 1)
            res = dfs(root.left, count) + dfs(root.right, count)
            if root.left == root.right:
                if count & (count - 1) == 0:
                    res += 1
            return res
        return dfs(root)
        
        
"""
Start time: 8:15PM
Learned some bit masking techniques. 
Strategy:  
used the observation that that a palindrome can only contain 
0000100010
you can have at most one unmatched pair.  
use xor
000010000 unmatched pair at 5


110
421
11
21



"""