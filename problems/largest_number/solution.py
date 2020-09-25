from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        nums=[str(x) for x in nums]
        def comparator(x,y):
            if x+y>y+x:
                return -1
            elif y+x>x+y:
                return 1
            return 0
        nums.sort(key=cmp_to_key(comparator))
        return str(int("".join(map(str,nums))))
        