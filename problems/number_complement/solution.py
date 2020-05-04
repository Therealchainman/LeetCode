class Solution:
    def findComplement(self, num: int) -> int:
        cut = 1
        while num*2 > cut:
            num = num ^ cut
            cut = cut << 1
        return num
            