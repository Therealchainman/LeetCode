class Solution:
    def repeatedSubstringPattern(self, s):
        n=len(s)
        pattern=[0]*n
        # start the substring as first character in string
        i,idx=1,0
        while i<n:
            if s[i]==s[idx]:
                idx+=1
                pattern[i]=idx
                i+=1
            else:
                if idx>0:
                    idx=pattern[idx-1]
                else:
                    i+=1
        return True if pattern[-1] and pattern[-1]%(n-pattern[-1])==0 else False

                    
"""
KMP algorithm implementation
"ababba"
     ab
"""
        