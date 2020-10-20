"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        root=node
        nodeCopy=Node(node.val)
        dq=deque([node])
        D={node:nodeCopy}
        while dq:
            node=dq.popleft()
            for n in node.neighbors:
                if n not in D:
                    nodeCopy=Node(n.val)
                    D[n]=nodeCopy
                    D[node].neighbors.append(nodeCopy)
                    dq.append(n)
                else:
                    D[node].neighbors.append(D[n])
        return D[root]
            