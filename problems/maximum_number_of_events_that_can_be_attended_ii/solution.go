var dp [][]int

func max(x, y int) int {
    if x > y {return x}
    return y
}

func maxValue(events [][]int, k int) int {
    dp = make([][]int,len(events)+1)
    for i:=0;i<len(events)+1;i++{
        dp[i] = make([]int,k+1)
        for j:=0;j<k+1;j++{
            dp[i][j]=-1
        }
    }
    sort.SliceStable(events, func (i, j int) bool {
        if events[i][0]!=events[j][0]{
            return events[i][0]<events[j][0]
        }
        return events[i][1]<events[j][1]
    })
    return backtrack(events,0,k)
}

func backtrack(events [][]int, eventi int, k int) int {
    if k==0 || len(events)<=eventi {
        return 0
    }
    if dp[eventi][k]!=-1{
        return dp[eventi][k]
    }
    var i int
    for i=eventi+1;i<len(events);i++{
        if events[i][0]>events[eventi][1]{
            break
        }
    }
    dp[eventi][k]=max(backtrack(events,eventi+1,k),events[eventi][2]+backtrack(events,i,k-1))
    return dp[eventi][k]
}