const m = 100001 
var BIT [m]int
func update(x int) {
    for x<m {
        BIT[x]++
        x += (x&-x)
    }
}

func sum(x int) int {
    res := 0
    for x>0 {
        res+=BIT[x]
        x -= (x&-x)
    }
    return res
}

func min(x, y int) int {
    if x < y{
        return x
    }
    return y
}

func createSortedArray(instructions []int) int {
    const mod = 1000000007
    for i,_ := range BIT {
        BIT[i]=0
    }
    cost := 0
    for i, v := range instructions {
        cost = (cost + min(sum(v-1),i-sum(v)))
        update(v)
    }
    return cost%mod
}