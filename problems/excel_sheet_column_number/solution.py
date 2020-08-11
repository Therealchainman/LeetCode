class Solution:
    def titleToNumber(self, s):
        res=0
        n=len(s)
        for i in range(n-1,-1,-1):
            res+=pow(26,i)*(ord(s[n-i-1])-ord("A")+1)
        return res
        
        # res = 0
        # for i in s:
        #     res = res*26 + ord(i)-ord('A')+1
        # return res
            
        