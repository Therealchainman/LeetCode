# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root,key):
        cur=root
        def dfs_left(node):
            cur=node
            while cur.left:
                cur=cur.left
            return cur
        parent=cur
        while cur:
            if cur.val==key:
                if parent is cur:
                    if cur.right:
                        root=cur.right
                        dfs_left(root).left=cur.left   
                    else:
                        root=cur.left
                elif cur.right:
                    if parent.val>cur.val:
                        parent.left=cur.right
                        dfs_left(cur.right).left=cur.left
                    else:
                        parent.right=cur.right
                        dfs_left(cur.right).left=cur.left
                else:
                    if parent.left and parent.left.val==key:
                        parent.left=cur.left
                    else:
                        parent.right=cur.left
                break
            parent=cur
            if key<cur.val:
                cur=cur.left
            else:
                cur=cur.right
        return root
        