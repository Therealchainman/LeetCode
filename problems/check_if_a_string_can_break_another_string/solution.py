from collections import Counter
class Solution:
    def check(self, d1, d2):
        breaks = 0
        for char in "abcdefghijklmnopqrstuvwxyz":
            breaks += d1[char] - d2[char]
            if breaks < 0:
                return False
        return True
            
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        d2 = Counter(s2)
        return self.check(d1, d2) | self.check(d2, d1)

                
                