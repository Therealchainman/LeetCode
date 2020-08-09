class Solution:
    def makeGood(self, S):
        n=len(S)
        if n==1:
            return S
        S=list(S)
        i=0
        while i+1<len(S):
            if S[i].isupper() and S[i+1].islower():
                if S[i].lower() == S[i+1].lower():
                    S.pop(i+1)
                    S.pop(i)
                    i=0
                else:
                    i+=1
            elif S[i+1].isupper() and S[i].islower():
                if S[i].lower() == S[i+1].lower():
                    S.pop(i+1)
                    S.pop(i)
                    i=0
                else:
                    i+=1
            else:
                i+=1
        return "".join(S)