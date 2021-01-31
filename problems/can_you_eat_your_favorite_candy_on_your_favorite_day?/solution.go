func canEat(candiesCount []int, queries [][]int) []bool {
    n := len(candiesCount)
    prefix := make([]int, n+1)
    for i:=1;i<n+1;i++ {
        prefix[i] = prefix[i-1]+candiesCount[i-1]
    }
    var candy int
    var day int 
    var dcap int
    ans := make([]bool, len(queries))
    var earliest int
    var latest int
    var minTake int
    var maxTake int
    for i, q := range queries {
        candy = q[0]
        day = q[1]
        dcap = q[2]
        minTake = day + 1
        maxTake = (day + 1)*dcap - 1
        latest = prefix[candy+1]
        earliest = prefix[candy]
        if earliest > maxTake || latest < minTake {
            ans[i] = false
        } else {
            ans[i] = true
        }
    }
    
    return ans
}