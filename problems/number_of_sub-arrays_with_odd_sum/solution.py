class Solution:
    def numOfSubarrays(self, A) -> int:
        
        P = [0]
        for x in A:
            P.append(P[-1] + x)
            
        # First step is to calculate the prefix sums of A
        # A = [1,2,3,4]
        # P = [0,1,3,6,10]
        
        #All subarray sums: P[j] - P[i] for i < j
        # Number of i < j with P[j] - P[i] = 1 (mod 2)
        # For j:
        #    Find number of P[i] != P[j] (mod 2)
        
        ans = even = odd = 0
        for s in P:
            if s & 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % (10**9 + 7)
        # MOD = 10**9 + 7
        # n = len(arr)
        # temp = [1, 0]
        # res = 0
        # for v in arr:
        #     res = (res + v) % 2
        #     temp[res] += 1
        # return temp[0]*temp[1] % MOD
            
                
                