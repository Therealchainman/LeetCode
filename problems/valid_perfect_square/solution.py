class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0 
        r = num
        while r > l:
            mid = (r + l) >> 1
            square = mid * mid
            if square >= num:
                r = mid
            else:
                l = mid + 1
        return r * r == num