class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')]*amount
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
        
"""
Start time: 6:15pm
a) knapsack unbounded (repetition)
1) I neeed to retun the combinations, so yeah return the one with fewest number coins. 
2) 

"""