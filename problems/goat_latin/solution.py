class Solution:
    def toGoatLatin(self, S):
        V=set("aeiouAEIOU")
        def goat(w,i):
            if w[0] not in V:
                w=w[1:]+w[0]
            w+="ma"+"a"*(i+1)
            return w
        return " ".join(goat(w,i) for i,w in enumerate(S.split()))
        