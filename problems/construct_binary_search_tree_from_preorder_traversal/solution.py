# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and root.val > preorder[i]:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

        
"""
Start time: 6:20PM
a) preorder = [8,5,1,7,10,12] 
root = 8
i = 1, root.val = 8, preorder[1] = 5
i = 2
i = 3
i = 4, root.val = 8, preorder[4] = 10 
root.left = preorder = [5, 1, 7]
root.right = preorer = [10, 12]

"""