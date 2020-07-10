"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        stack = [head]
        prev = Node(0)
        while stack:
            node = stack.pop()
            node.prev = prev
            prev.next = node
            prev = node
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
        head.prev = None
        return head
    
                
        
"""
Start time: 12:37PM
approach1:  Greedy - single pass
maybe use a deque, 
using a queue in this problem 
Let's do a DFS search algorithmic approach
Basically just need to search down


"""