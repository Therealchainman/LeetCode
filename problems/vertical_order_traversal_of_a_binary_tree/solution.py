# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root):
        dq=deque([(0,0,root)])
        res = []
        while dq:
            x, y, node = dq.popleft()
            res.append((x,y,node.val))
            if node.left:
                dq.append((x-1,y-1,node.left))
            if node.right:
                dq.append((x+1,y-1,node.right))
        res.sort(key=lambda x: [x[0],-x[1],x[2]])
        p = float('inf')
        idx = -1
        ans = []
        for x, y, v in res:
            if x != p:
                ans.append([v])
                idx += 1
                p = x
            else:
                ans[idx].append(v)
        return ans
            
            

"""
start time: 7:25PM
approach1: BFS + sort
"""