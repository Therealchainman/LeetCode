func max(x int, y int) int {
    if x>y {
        return x
    }
    return y
}

func min(x int, y int) int {
    if x>y {
        return y
    }
    return x
}

func score(turn string, le int, ri int, stones []int, value int,memo [][]int) int {
    if le>ri {
        return 0
    }
    if memo[le][ri] != 0 {
        return memo[le][ri]
    }
    var nextTurn string
    if turn == "A" {
        nextTurn = "B"
    } else {
        nextTurn = "A"
    }
    var finalScore int
    rightScore := score(nextTurn, le+1,ri,stones, value-stones[le],memo)
    leftScore := score(nextTurn, le, ri-1, stones, value-stones[ri],memo)
    if turn=="A" {
        finalScore = max(rightScore-stones[le],leftScore-stones[ri]) + value
    } else {
        finalScore = min(rightScore+stones[le],leftScore+stones[ri]) - value
    }
    memo[le][ri]=finalScore
    return memo[le][ri]
}

func sum(stones []int) int {
    ans := 0
    for _,x := range stones {
        ans+=x
    }
    return ans
}
func stoneGameVII(stones []int) int {
    n := len(stones)
    memo := [][]int{}
    for i:=0;i<n;i++ {
        memo = append(memo,[]int{})
    }
    fmt.Println(len(memo))
    for i:=0;i<n;i++ {
        for j:=0;j<n;j++ {
            memo[i] = append(memo[i], 0)
        }
    }
    return score("A", 0,n-1,stones, sum(stones),memo)
}