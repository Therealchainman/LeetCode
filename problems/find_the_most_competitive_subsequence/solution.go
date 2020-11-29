func mostCompetitive(nums []int, k int) []int {
    ans := []int{}
    numRemove := len(nums) - k
    for _,x := range nums {
        for len(ans)>0 && x<ans[len(ans)-1] && numRemove>0 {
            ans[len(ans)-1]=0
            ans = ans[:len(ans)-1]
            numRemove--
        }
        ans = append(ans, x)
    }
    for numRemove>0 {
        ans[len(ans)-1]=0
        ans = ans [:len(ans)-1]
        numRemove--
    }
    return ans
}