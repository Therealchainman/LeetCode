class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        def helper(n: int) -> bool:
            sum = 0
            if n == 1:
                return True
            if n in nums:
                return False
            nums.add(n)
            while n > 0:
                sum += (n % 10)**2
                n = n//10
            return helper(sum)
        return helper(n)