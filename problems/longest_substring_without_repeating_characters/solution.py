from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        "dvdf", so start with string "dvdf" and count until you get repeat
        then call with string "vdf" and count until you get repeat or reach the end of the string. 
        Then call with "df", meh sure.  
        queue = [d]
        so 1 + counter("vdf")
        queue = [dv]
        2
        '''          
        start = length = 0
        queue = {}
        for i, c in enumerate(s):
            if c in queue and start <= queue[c]:
                start = queue[c] + 1
            else:
                length = max(length, i - start + 1)
            queue[c] = i
        return length
                
            