from collections import defaultdict
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = defaultdict(WordDictionary)
        self.isWord = False
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        self.add(word, 0)
        
    def add(self,word, p):
        if p == len(word):
            self.isWord = True
        else:
            self.children[word[p]].add(word,p+1)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(word, 0)
            
            
    def dfs(self, word, p):
        if p == len(word):
            return self.isWord

        if word[p] in self.children.keys():
            return self.children[word[p]].dfs(word, p + 1)
        if word[p] == ".":
            for wd in self.children.values():
                if wd.dfs(word, p + 1):
                    return True
        return False
        
"""
Start time: 5:25PM

approach1:  Trie Datastructure


"""

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)