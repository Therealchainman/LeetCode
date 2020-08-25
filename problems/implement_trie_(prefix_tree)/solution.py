class TrieNode:
    
    def __init__(self):
        self.children={}
        self.isWord=False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.isWord=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.dfs(word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.dfs(prefix,1)
        
    def dfs(self,word,version=0):
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True if version==1 else cur.isWord

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)