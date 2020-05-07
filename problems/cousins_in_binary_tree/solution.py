# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from collections import defaultdict

class Solution:
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool: 
        dictionary = defaultdict()
        doubleQueue = deque([(root, 0, 0)])
        while doubleQueue:
            node, depth, parent = doubleQueue.popleft()
            if node.val == x or node.val == y:
                dictionary[node.val] = (depth, parent)
            if node.left:
                doubleQueue.append((node.left, depth + 1, node.val))
            if node.right:
                doubleQueue.append((node.right, depth + 1, node.val))
        if dictionary[x][0] == dictionary[y][0] and dictionary[x][1] != dictionary[y][1]:
            return True
        return False
            
        
'''
       1
    2     3
        4
Find the depth, and find the parents of the two values.  Since it is is 
x = 2, y = 3
How can you find the parent node

'''