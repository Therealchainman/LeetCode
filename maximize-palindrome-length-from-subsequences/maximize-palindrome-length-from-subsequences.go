var dp [][]int

func recurse(i int, j int, s string) int {
    if j<i {return 0}
    if j==i {
        dp[i][j]=1
        return dp[i][j]
    }
    if dp[i][j]!=0 {
        return dp[i][j]
    }
    if s[i]==s[j] {
        dp[i][j]=recurse(i+1,j-1,s)+2
        return dp[i][j]
    }
    dp[i][j]=max(recurse(i+1,j,s),recurse(i,j-1,s))
    return dp[i][j]
}

func longestPalindrome(word1 string, word2 string) int {
    n, m := len(word1), len(word2)
    N := n+m
    dp = nil
    ret := 0
    for i:=0;i<N;i++{
        f:=make([]int,N)
        dp = append(dp, f)
    }
    recurse(0,N-1,word1+word2)
    for i:=0;i<n;i++{
        for j:=0;j<m;j++{
            if word1[i]==word2[j] {
                ret=max(ret,dp[i+1][n+j-1]+2)
            }
        }
    }
    return ret
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
