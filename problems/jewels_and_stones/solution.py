class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        count = 0
        print(jewels)
        for x in S:
            if x in jewels:
                count += 1
        return count