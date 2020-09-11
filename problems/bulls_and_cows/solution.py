from collections import Counter
class Solution:
    def getHint(self, secret, guess):
        A=sum(i==j for i,j in zip(secret,guess))
        s,g=Counter(secret),Counter(guess)
        B=sum((s&g).values())-A
        return f"{A}A{B}B"