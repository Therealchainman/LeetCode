class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dict = dict()
        self.isRemoved = set()
        self.head = None
        self.tail = None
        for x in nums:
            node = Node(x)
            self.addNode(node)
        
    def showFirstUnique(self) -> int:
        if self.head is not None:
            return self.head.data
        return -1
        
    def add(self, value: int) -> None: 
        node = Node(value)
        self.addNode(node)
    
    def addNode(self, node) -> None:
        if self.head is None and node.data not in self.isRemoved:
            self.head = node
            self.tail = node
            self.dict[node.data] = node
        else:
            if node.data in self.dict:
                if node.data not in self.isRemoved:
                    self.removeNode(self.dict[node.data])
            else:
                prev_tail = self.tail
                node.prev = prev_tail
                prev_tail.next = node
                self.tail = node
                self.dict[node.data] = node
        
    def removeNode(self, node) -> None:
        self.isRemoved.add(node.data)
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        next_node = node.next
        prev_node = node.prev
        if prev_node is not None:
            prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node
        
class Node:
    
    def __init__(self, value: int):
        self.next = None
        self.prev = None
        self.data = value
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)