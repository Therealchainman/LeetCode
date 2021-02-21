func recurse(nums []int, mult []int, le int, i int, A *[][]int) int {
    dp := *A
    if i>=len(mult) {
        return 0
    }
    if dp[le][i]==0{
        ri := len(nums)-1-(i-le)
        leftMax := nums[le]*mult[i]+recurse(nums,mult,le+1,i+1,&dp)
        rightMax := nums[ri]*mult[i]+recurse(nums,mult,le,i+1,&dp)
        dp[le][i]=max(leftMax,rightMax)
    }
    return dp[le][i]
}

func maximumScore(nums []int, multipliers []int) int {
    m := len(multipliers)
    dp := make([][]int,m+1)
    for i := range dp {
        dp[i] = make([]int, m+1)
    }
    return recurse(nums,multipliers,0,0,&dp)
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}