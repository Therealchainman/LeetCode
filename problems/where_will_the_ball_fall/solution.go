func findBall(grid [][]int) []int {
    m := len(grid)
    n := len(grid[0])
    ans := make([]int, n)
    for i:=0;i<n;i++ {
        pos := i
        lv := 0
        ans[i]=-1
        for pos >= 0 && pos < n {
            if lv==m {
                ans[i]=pos
                break
            }
            if pos<n-1 && grid[lv][pos]==1 && grid[lv][pos+1]==-1 {
                break
            } else if pos>0 && grid[lv][pos]==-1 && grid[lv][pos-1]==1 {
                break
            } else if grid[lv][pos]==1 {
                pos++
            } else if grid[lv][pos]==-1 {
                pos--
            }
            lv++
        }
    }
    return ans
}