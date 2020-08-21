class Solution:
    def sortArrayByParity(self, A):
        odd, even = [],[]
        for a in A:
            if a%2==0:
                even.append(a)
            else:
                odd.append(a)
        ans=even+odd
        return ans
        