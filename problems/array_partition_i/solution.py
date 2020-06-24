class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


"""
Start time: 9:07PM
approach1:  Naively using counting sort
time: O(n + k), space: O(n + k)
-10000 -> 10000 --> 20000, and suppose your array is size 4
O(4 + 20000)

notice not efficient because the range can be very very large like say way larger than n so k >> n
suppose k = n^10
then O(n + n^10) is like O(n^10).  It seems counting sort is only really useful when the range is samall.  

approach2: O(nlogn) + O(n + k) + O(k) = O(nlogn)
slicing is O(n+k) where k is length of slice. 


[1,4,3,2]
[1,2,3,4]
sum of the even indexed values so take 1 + 3 = 4
1) sort,  O(nlogn)
2) sum up over the even indices, like 0,2 O(n/2) = O(n)

[1,1,1,1]
1+1=2



[1,1]

[0]

count[0] += 1
[2]
i = 1
i = 0
count[1] = count[0]
[1,2]
ans =[0,0]
ans[count[0]]= 
[1,0]


[1,4,3,2]
[1,2,3,4]
min(1,2) + min(3,4) = 4

[1,2,1,2,3,4,7,7]
[1,1,2,2,3,4,7,7]
min(1,1) + min(2,2) + min(3,4) + min(7,7) = 13

[-1,2,-3,4,5,9,-7,-10]
[-10,-7,-3,-1,2,4,5,9]
-10-3+2+5 = -5

1) taking 1 + 2 + 3 + 7 , I could iterate by going through all the even index values and summing those O(n)
2) Counting sort which I believe is O(n + k) --> k?
3) 
               
"""
        