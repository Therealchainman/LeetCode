class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        res = 0 
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[i] - arr[k]) <= c and abs(arr[j] - arr[k]) <= b:
                            res += 1
        return res
                    
                        
        