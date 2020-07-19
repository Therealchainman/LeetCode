class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        e = numBottles
        while numBottles > 0:
            ex = numBottles // numExchange
            e += ex
            ext = numBottles % numExchange if numExchange < numBottles else 0
            numBottles = ex + ext
        return e