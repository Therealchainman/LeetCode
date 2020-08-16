class Solution:
    def threeConsecutiveOdds(self, A):
        c=0
        for a in A:
            if a%2!=0:
                c+=1
            else:
                c=0
            if c==3:
                return True
        return False
        