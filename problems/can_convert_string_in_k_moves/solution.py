class Solution:
    def canConvertString(self,S,T,k):
        if len(S)!=len(T):
            return False
        
        count=[0]*26
        for s,t in zip(S,T):
            shift=(ord(t)-ord(s))%26
            if shift:
                count[shift]+=1
        m=max(count)
        for i in range(25,-1,-1):
            if count[i]==m:
                break
        return (m-1)*26+i<=k
        
            
        
        