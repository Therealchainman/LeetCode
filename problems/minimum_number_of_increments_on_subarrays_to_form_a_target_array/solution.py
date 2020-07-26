class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None
        self.dead = False
        
    def leave(self):
        self.dead = True
        Node.stitch(self.prev, self.next)
        
    @staticmethod
    def stitch(*nodes):
        for i in range(len(nodes)-1):
                      nodes[i].next = nodes[i+1]
                      nodes[i+1].prev = nodes[i]
        
class DLL:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def push(self, val):
        node = Node(val)
        node.stitch(self.tail.prev, node, self.tail)
        return node

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # Doubly Linked List solution
        # [1,2,2,3,3,3,4,4,4,4,4] - > [1,2,3,4] groupify
        A = [k for k, _ in itertools.groupby(target)]
        dll = DLL()
        nodemap = defaultdict(list)
        for x in A:
            node = dll.push(x)
            nodemap[x].append(node)
        ans = 0
        for v in range(max(A), 0, -1):
            for node in nodemap[v]:
                if node.dead:
                    continue
                # lv=4, v=9, rv=5
                lv = node.prev.val
                rv = node.next.val
                mx = max(lv, rv)
                ans += v - mx
                node.val = mx
                if mx:
                    if lv == mx:
                        node.prev.leave()

                    if rv == mx:
                        node.next.leave()
        
                nodemap[mx].append(node)
            
        return ans
        
        # ops = 0
        # prev = 0
        # for t in target:
        #     ops += max(t - prev, 0)
        #     prev = t
        # return ops
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

            
        