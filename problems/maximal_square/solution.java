class Solution {
    public int maximalSquare(char[][] matrix) {
        int n= matrix.length;
        if (n == 0) {
            return 0;
        }
        char[] first_row = matrix[0];
        int m = first_row.length;
        int[][] dp = new int[n + 1][m + 1];
        int max_side = 0;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (matrix[r][c] == '1') {
                    dp[r + 1][c + 1] = Math.min(Math.min(dp[r][c], dp[r][c + 1]), dp[r+1][c]) + 1;
                    max_side = Math.max(max_side, dp[r+1][c+1]);
                }
            }
        }
        return max_side*max_side;
    }
}