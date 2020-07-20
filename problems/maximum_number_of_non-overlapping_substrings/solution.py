from collections import defaultdict
class Solution:
    def maxNumOfSubstrings(self, s):
        intervals = defaultdict(list)
        for i, c in enumerate(s):
            intervals[c].append(i)
        for key, interv in intervals.items():
            left, right = interv[0], interv[-1] + 1
            tl, tr = left, right
            left, right = -1, -1
            # cont = True
            while tl != left or tr != right:
                left, right = tl, tr
                for ch in set(s[tl:tr]):
                    tl = min(tl, intervals[ch][0])
                    tr = max(tr, intervals[ch][-1] + 1)
                # cont = False if tl == left and tr == right else True
            intervals[key] = [left, right]
        sint = sorted(intervals.values(), key=lambda pair: pair[1])
        prev = 0
        output = []
        for start, end in sint:
            if start >= prev:
                output.append(s[start:end])
                prev = end
        return output
                
            
        
                    
                        
        
"""
approach1:  iterating

"abbaccd"
 ^     ^

"""