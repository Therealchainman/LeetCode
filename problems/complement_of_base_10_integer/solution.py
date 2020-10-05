class Solution:
    def bitwiseComplement(self, N):
        if N==0:
            return 1
        bits_len=N.bit_length()
        for i in range(bits_len):
            N^= (1<<i)
        return N
        