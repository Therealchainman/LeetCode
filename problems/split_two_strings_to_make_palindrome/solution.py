class Solution:
    def checkPalindromeFormation(self, S,T):
        n=len(T)
        
        def isPali(S,i,j):
            return all(S[i+k]==S[j-k] for k in range(j-i+1>>1))
        
        # Checking prefix and suffix are equal to each other until they are no longer.  
        def prefixes(S,T):
            
            i,j=0,n-1
            while i<j and S[i]==T[j]:
                i+=1
                j-=1
            
            return isPali(S,i,j) or isPali(T,i,j)
        
        return prefixes(S,T) or prefixes(T,S)
        