class TrieNode:
    def __init__(self):
        self.edges={}
        self.empty=True

    def add_edge(self,edge):
        if not self.has_edge(edge):
            self.edges[edge]=TrieNode()

    def has_edge(self,edge):
        return edge in self.edges

    def get_edge(self,edge):
        return self.edges[edge]

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def add(self,binary_number):
        cur_node=self.root
        cur_node.empty=False
        for offset in range(31,-1,-1):
            if binary_number & (1<<offset)>0:
                cur_node.add_edge("1")
                cur_node=cur_node.get_edge("1")
            else:
                cur_node.add_edge("0")
                cur_node=cur_node.get_edge("0")

    def get_max_xor(self,binary_number):
        prev=0
        cur_node=self.root
        if cur_node.empty:
            return 0
        for offset in range(31,-1,-1):
            if (binary_number & (1<<offset))>0:
                if cur_node.has_edge("0"):
                    cur_node=cur_node.get_edge("0")
                else:
                    cur_node=cur_node.get_edge("1")
                    prev+=2**offset
            else:
                if cur_node.has_edge("1"):
                    cur_node=cur_node.get_edge("1")
                    prev+=2**offset
                else:
                    cur_node=cur_node.get_edge("0")
        return prev^binary_number

class Solution:
    def findMaximumXOR(self, nums):
        trie=Trie()
        max_xor=0
        for num in nums:
            max_xor=max(max_xor,trie.get_max_xor(num))
            trie.add(num)
        return max_xor
