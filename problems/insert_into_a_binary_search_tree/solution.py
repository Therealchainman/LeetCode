# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        cur_node=root
        while cur_node:
            if val>cur_node.val:
                if not cur_node.right:
                    cur_node.right=TreeNode(val)
                    break
                cur_node=cur_node.right
            else:
                if not cur_node.left:
                    cur_node.left=TreeNode(val)
                    break
                cur_node=cur_node.left
        return root