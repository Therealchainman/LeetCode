from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A):
        inf=float('inf')
        best=-inf
        for a in permutations(A):
            h1,h2,m1,m2=a
            hours=h1*10+h2
            minutes=m1*10+m2
            
            if 0<=hours<=23 and 0<=minutes<=59:
                best=max(best, 60*hours+minutes)
        if best==-inf:
            return ""
        minutes=str(best%60)
        hours=str(best//60)
        return f"{hours.zfill(2)}:{minutes.zfill(2)}"