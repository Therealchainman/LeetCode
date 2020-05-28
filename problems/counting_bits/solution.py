class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0 for _ in range(num + 1)]
        offset = 1
        for i in range(1, num + 1):
            if 2 * offset == i:
                offset *= 2
            ans[i] = ans[i - offset] + 1
        
        return ans
        
            
        
        
        
"""
Start time: 6:06AM
how to do in linear time? 

"""