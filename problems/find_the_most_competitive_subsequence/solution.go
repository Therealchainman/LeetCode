func mostCompetitive(nums []int, k int) []int {
    var ans []int
    var p int
    for i, x := range nums {
        p = len(nums)-i
        for len(ans)>0 && x < ans[len(ans)-1] && p - (k - len(ans)) > 0 {
            ans = ans[:len(ans)-1]
        }
        if len(ans) < k {
            ans = append(ans, x)
        }
    }
    return ans
}