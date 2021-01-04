func dfs(index int, visited map[int]bool, end int) int {
    if index>end {
        return 1
    }
    ans := 0
    for perm:=1;perm<=end;perm++ {
        if (perm%index==0 || index%perm==0) && !visited[perm] {
            visited[perm]=true
            ans+=dfs(index+1,visited,end)
            visited[perm]=false
        }
    }
    return ans
}
func countArrangement(n int) int {
    visited := make(map[int]bool)
    return dfs(1,visited,n)
}