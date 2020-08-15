class Solution:
    def selfDividingNumbers(self, l,r):
        isSelfDividing = lambda a: '0' not in str(a) and all(a % int(d) == 0 for d in str(a))
        return filter(isSelfDividing, range(l,r+1))
        