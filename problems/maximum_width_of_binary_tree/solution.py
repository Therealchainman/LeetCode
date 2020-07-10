# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = deque()
        q.append([root, 0])
        maxWidth = 1
        while q:
            init_idx = q[0][1]
            end_idx = q[-1][1]
            maxWidth = max(maxWidth, end_idx - init_idx + 1)
            for i in range(len(q)):
                node, val = q.popleft()
                idx = val - init_idx
                if node.left:
                    q.append([node.left, 2*idx + 1])
                if node.right:
                    q.append([node.right, 2*idx + 2])
        return maxWidth
                
                
            
"""
Start time: 8:41PM
approach1:
 
"""