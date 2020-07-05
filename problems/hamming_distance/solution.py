class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")
        
        
"""
No mic, but solving this problem with bitwise operations: 

So in order to track number of bits that differ
We can use the xor operation because it will turn a bit on (1) if the bits are different in the two numbers
so 
1^4 = 0101

Then we can count the number of bits that are in the 1s. 
We can either set  or clear the least significant bit or the most significant bit.

One method is to clear the LEAST significant bit by doing this
take the result which is 5 = 0101
now what is 
5 & 4 = That is 0101 & 0100 = 0100
now what is 4 & 3 = 0100 & 0011 = 0000
So basically we can keep taking n & (n - 1) to clear each least significant bit. 
We just need to count the number of times.  

"""