from collections import deque
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1
    
    
    '''
    [1,1,1,0,0,0,1,1,1,1,0]
    K = 2
    j = 2, and K = 2, i = 0
    window pane = j - i + 1, sliding window size equals 3
    j = 3, K = 1, 
    j = 4, K = 0
    j = 5, K = -1
    set K = 0, 
    i = 1, 
    5-1+1=4
    j = 6
    size of window is 6
    i = 1
    [0,0,0,1]
    k 
    '''