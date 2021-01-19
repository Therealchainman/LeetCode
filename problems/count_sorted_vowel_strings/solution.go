func countVowelStrings(n int) int {
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, 6)
    }
    for j:=0;j<6;j++ {
        dp[0][j] = 1
    }
    for i:=1;i<=n;i++ {
        for j:=1;j<6;j++ {
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
        }
    }
    return dp[n][5]
}