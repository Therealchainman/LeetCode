func longestPalindromeSubseq(s string) int {
    n := len(s)
    dp := make([][]int,n)
    for i := range dp {
        dp[i] = make([]int,n)
    } 
    // A dp where we are considering the longest palindrome in every substring of s[i:j+1]
    for i:=n-1;i>=0;i--{
        dp[i][i]=1
        for j:=i+1;j<n;j++{
            if s[i]==s[j] {
                dp[i][j] = dp[i+1][j-1]+2
            } else {
                dp[i][j] = max(dp[i+1][j],dp[i][j-1]) // take the longest palindrome that started at i+1 index to j or i to j-1 index
            }
        }
    }
    print(dp)
    return dp[0][n-1]  // The longest palindrome in the substring s[i:n]
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
