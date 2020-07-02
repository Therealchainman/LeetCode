# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q, res = deque([(root, 0)]), []
        
        while q:
            node, height = q.popleft()
            if node:
                if height == len(res):
                    res.append([])
                res[height].append(node.val)
                if node.left:
                    q.append((node.left, height + 1))
                if node.right:
                    q.append((node.right, height + 1))
        return res[::-1]
        
"""
FIFO -> queue
res
[]
[[]]
[[3]]
[[3],[]]
[[3],[9,20],[]]

"""
        
