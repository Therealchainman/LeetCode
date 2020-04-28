class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        # rows by columns, so n = number of rows, m = number of columns
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        max_side = 0
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == '1':
                    dp[r + 1][c + 1] = min(dp[r][c], dp[r][c+1], dp[r+1][c]) + 1
                    max_side = max(max_side, dp[r+1][c+1])
        return max_side*max_side