class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
        
            
        
"""
Start time: 7:01PM
approach1: nlogn
sort array in descending
move k iterations to the index of the answer. 

approach2: O(n)
iterate through add all elements to the priority queue
pop from the priority queue k times

O(nlogn+logk)

logn+logn+logn 
--n times-----

[6,5,5,4,]


"""