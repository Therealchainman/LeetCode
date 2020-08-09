class Solution:
    def getMaxRepetitions(self, s1,x1,s2,x2):
        n2=len(s2)
        jump=[0]*n2
        for i in range(n2):
            for c in s1:
                if s2[(i+jump[i])%n2]==c:
                    jump[i]+=1
                    
        #linear finish
#         cur=0
#         for _ in range(x1):
#             cur+= jump[cur%n2]
#         return cur //n2 // x2
        
        # binary lifting (advanced)
        def add(j1,j2):
            ans=[]
            for i,x in enumerate(j1):
                ans.append(x+j2[(i+x)%n2])
            return ans
        jp=jump[:]
        ja=[0]*n2
        while x1:
            if x1 & 1:
                ja=add(ja,jp)
            jp=add(jp,jp)
            x1 >>= 1
        return ja[0]//n2//x2
        