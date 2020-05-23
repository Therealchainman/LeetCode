class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        visited = set()
        res = []
        for den in range(1, n + 1):
            for num in range(1, den):
                floatVal = num / den
                
                if floatVal not in visited:
                    visited.add(floatVal)
                    res.append("/".join(map(str, [num, den])))
        return res
        
"""
no gcd method:
start time: 9:32PM
"""