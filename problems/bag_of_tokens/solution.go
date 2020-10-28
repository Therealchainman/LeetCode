import "sort"

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

func bagOfTokensScore(tokens []int, P int) int {
    sort.Ints(tokens)
    var i = 0
    var j = len(tokens)-1
    var score = 0
    var res = 0
    for i<=j && P>0 && score>=0 {
        for i<=j && tokens[i]<=P {
            P-=tokens[i]
            score++
            i++
        }
        res=max(res,score)
        if i<=j {
            P+=tokens[j]
            j--
            score--
        }
    }
    return res
    
}