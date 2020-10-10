# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
        
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res=[]
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return " ".join(map(str,res))
            
    from collections import deque
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        A=deque(int(x) for x in data.split())
        inf=float('inf')
        def search(minVal,maxVal):
            if A and minVal<A[0]<maxVal:
                val=A.popleft()
                node=TreeNode(val)
                node.left=search(minVal,val)
                node.right=search(val,maxVal)
                return node
        return search(-inf,inf)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans