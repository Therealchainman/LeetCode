class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
#         def countingSort(A, d):
#             output = []
#             for i in range(10):
#                 for j in range(len(A)):
#                     temp = A[j]*10//d
#                     if temp % 10 == i:
#                         output.append(A[j])
#             return output
            
#         def radixSort(A):
#             ma = max(A)
#             div = 1
#             while ma//div > 0:
#                 div *= 10
#                 A = countingSort(A, div)
#             return A
#         nums = radixSort(nums)
        nums.sort()
        MOD = 10**9 + 7
        ans = 0
        j = len(nums) - 1
        for i, l in enumerate(nums):
            while j > i and nums[j] + l > target:
                j -= 1
            if nums[j] + l <= target:
                ans += pow(2, j-i, MOD)
        return ans % MOD
        
"""
Explore this pattern:
Challenge:
time to do the radix sort. 
So radix sort is like a counting sort for each digit.  So we need to count the number of digits and then use a counting sort
What does a counting sort do it searches through the range, and adds to the result in order.  

Try using a radix sort to get O(n+k) time 
and then use a something something lol. 
And then use a trick or two haha,  cause you sort, then you want
to use a type of sliding window. 

The major patterns:
ignoring the sorting part.  I want to figure out the sliding window component. 

take [3,5,6,7] -> [0,1,2,3]
What do we have here? 

Now we take the A[j] - A[i], 
if these are smaller than the target we are good.
A[j]-A[i] <= target.
If they are not then we want to move the i forward until it is smaller than target.
No we want to move the j my bad
So j starts at the right side, but moves to the left.  
The i starts on the right,  if it is ever to great we need to move to the left. 
Then we get 3,5,6
And this is perfect you know.  So uh we are done right? 
Looks good to me what is the computation

2^2 so 2^(j - i)
Okay, but what about
[3,3,6,8]
We move to i = 0, j = 2 as well, 
and then we satisfy condition.  
So then we say 2^2 = 4
once that works move the i forward and see if you continue to get results that work for first yo udon't but second you will 
get a 2^1 so add 2 to that result. 

What is this pattern it is the number of combinations or something let's explore

[0,1,2,3,4]
i=0
j=4
Now we would say 2^4 = 16 ways to do this or 16 combinations for being at least this size. 
I won't go through, suppose we mvoe j =3 now we are like 8 ways
then we move i = 1
[1,2,3] now we say 2^2 = 4 ways
[1,2,3], [1,3],[2,3],[1,2]
Then we might get [2,3] -> [2],[3] so there are 2 ways.  Seems right to me.  
and then 2^0 equals 1 okay let's code.  
"""