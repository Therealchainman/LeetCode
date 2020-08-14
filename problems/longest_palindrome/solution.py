from collections import Counter
class Solution:
    def longestPalindrome(self, S):
        C=Counter(S)
        odd=0
        for s in set(S):
            if C[s] % 2 !=0:
                odd+=1
        return len(S)-odd+1 if odd>0 else len(S)
            