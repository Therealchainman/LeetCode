from collections import Counter
class Solution:
    def minInsertions(self, s):
        bal = ans = 0
        for c in s:
            if c=="(":
                bal+=2
                if bal&1:
                    bal-=1
                    ans+=1
            else:
                bal-=1
            
            if bal<0:
                ans+=1
                bal+=2
                
        return ans +bal