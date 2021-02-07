func shortestToChar(s string, c byte) []int {
    var n = len(s)
    var res = make([]int,n)
    for i:=0;i<n;i++{
        if s[i]==c{
            res[i]=0
        } else {
            res[i]=n
        }
    }
    for i:=1;i<n;i++{
        res[i]=min(res[i],res[i-1]+1)
    }
    for i:=n-2;i>=0;i--{
        res[i]=min(res[i],res[i+1]+1)
    }
    return res
}

func min(x, y int) int {
    if x < y {return x}
    return y
}