# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getAllElements(self, r1,r2):
        ret=[]
        def bfs(root):
            if not root:
                return
            dq=deque([root])
            while dq:
                node=dq.popleft()
                ret.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            return ret
        bfs(r1)
        bfs(r2)
        ret.sort()
        return ret
            
        