class Solution:
    def minSwaps(self, G):
        n = len(G)
        start = 1
        zeros = n - 1
        swaps = 0
        for i in range(n):
            temp = i
            while temp < n and G[temp][start:] != [0]*zeros:
                temp += 1
                
            if temp == n:
                return -1
            
            start += 1
            zeros -= 1

            while temp > i:
                G[temp], G[temp - 1] = G[temp - 1], G[temp]
                temp -= 1
                swaps += 1
                
        return swaps
        
                
        