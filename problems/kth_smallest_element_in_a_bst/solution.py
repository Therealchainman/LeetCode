# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        nodes = []
        def dfs(root):
            nonlocal stack, nodes
            if root:
                stack.append(root)
                dfs(root.left)
                dfs(root.right)
            elif not root and stack:
                nodes.append(stack.pop())
            return nodes
        return dfs(root)[k - 1].val