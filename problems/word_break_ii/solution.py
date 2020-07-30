from collections import defaultdict
class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        memo = defaultdict(list)
        wordDict = set(wordDict)
        breakable = [False]*(n + 1)
        breakable[0] = True
        for i in range(n + 1):
            for j in range(i):
                if breakable[j] and s[j:i] in wordDict:
                    breakable[i] = True
        if not breakable[-1]:
            return []
        return self.dp(s, wordDict, memo)
    
    def dp(self, s, wordDict, memo):
        if not s:
            return []
        if memo[s]:
            return memo[s]
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                rest = self.dp(s[len(word):], wordDict, memo)
                for w in rest:
                    w = word + " " + w
                    res.append(w)
        memo[s] = res
        return memo[s]
            
        
        
        
"""
approach1:  Brute force

rest = ["dog"]
s = "catsand"
word = "sand"

"""