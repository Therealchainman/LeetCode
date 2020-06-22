class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            onec = num & one
            twoc = num & two
            one = (one ^ onec) | (num ^ onec ^ twoc)
            two = (two ^ twoc) | onec
        return one
        
        
        
        
"""
Start time: 3:00 AM
approach1: Time -> O(n), Space -> O(1)
input = [2,2,3,2]
[00010, 00010, 00011, 00010]
1) Use mod 3 in a sense
2) promote from 0s to 1s, promote 1s to 2s, promote 2s to 0s
x=00010
one = 00010
two = 00000

x=00010
one = 00000
two = 00010

x=00011
one=00001
two=00000

x=00010
one=00011
two=00000

onec= one & x, twoc = two & x
one = one ^ onec | (x ^ onec ^ twoc)
two = two ^ twoc | onec

x=00011
one = 00010
onec = 00010
one = 00000
x^onec^twoc = 00001

two = 00100
twoc=00000
two=00110



00010-> 00020 -> 00001 -> 00011

0,1,2
00011

"""