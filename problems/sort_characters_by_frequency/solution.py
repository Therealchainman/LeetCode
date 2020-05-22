from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        ordered = sorted(counter.items(), key=lambda x: -x[1])
        return "".join(r*c for r, c in ordered)
        
""" 
b) Priority Queue
1) Iterate through string 
2) If element is not in my priority queue initialize it with the priority value of 1
3) if element already in it just pop it from priority queue and increment the priority value by 1. 
4) iterate through priority queue and pop every single elemtn out and return a string. 
5) Time complexity O(nlogn), space complexity O(n)
"""