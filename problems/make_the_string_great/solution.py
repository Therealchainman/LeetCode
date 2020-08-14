class Solution:
    def makeGood(self, S):
        while True:
            for i in range(1,len(S)):
                if S[i]!=S[i-1] and S[i].lower()==S[i-1].lower():
                    S=S[:i-1]+S[i+1:]
                    break
            else:
                break
        return S
            
        