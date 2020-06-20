class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort() #nlogn
        h = 0
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) >> 1
            if n - mid <= citations[mid]:
                h = max(h, n - mid)
                right = mid - 1
            else:
                left = mid + 1
        return h
            
        
"""

[0,0]

left = 0
right = 1
mid = 0
n-mid = 2
citations[mid] = 11
say at least we have 2 elements with at least 2 citations or more.  
h=2






Start time: 5:12PM
Approach1:  
understand: h-index
[10,20,30,20,20], N=5= number of papers
h = 10
5 - 10 = -5


[2,4,4,4,4]
 ^       ^
 

5 papers
3 papers with at least 3 citations.  
then 2 papers with no more than 3 citations.  

h = 1

5 --> 5 -5 = 0 so you have 0 papers,  with no more than 5 citations.  and you have 2 papers 

if you say h = 1
1 paper with at least 1 citation and the rest have no more than 1 citation.  

1) sort the array in ascending order nlogn time complexity
2) Binary search 
3) take the mid and see if it satisfies the conditions.  Where 
4) 

"""