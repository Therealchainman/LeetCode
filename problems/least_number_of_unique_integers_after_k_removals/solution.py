from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        arrSet = set(arr)
        heap = []
        for a in arrSet:
            heap.append([a, count[a]])
        heap.sort(key=lambda x: x[1], reverse=True)
        for _ in range(k):
            heap[-1][1] -= 1
            if heap[-1][1] == 0:
                heap.pop()
        return len(heap)
        
        
"""
Another thing look at this example:
[4,3,1,1,3,3,2]
So I remove 3 elements, what is the least number of unique integers.  Well remove the 4 and 2 and you can get it to 2.  

1) Sort the heap according to the priority, set reverse=True so it is in descending order, so that I reduce prirority of numbers that 
appear the fewest number of times.  I want to remove those first after all.  
2) get the elem and priority of the last element in heap
3) decrement the priority, if the priority==0, then pop it from the heap. 

"""