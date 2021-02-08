func minAbsDifference(nums []int, goal int) int {
    var n = len(nums)
    var half = n/2
    var minAbs = int(1e9+7)
    var X, Y = nums[half:], nums[:half]
    var xsum, ysum = make(map[int]bool), make(map[int]bool) 
    subsetSums(X,0,0,xsum)
    subsetSums(Y,0,0,ysum)
    var xrr, yrr = flatten(xsum), flatten(ysum)
    sort.Ints(yrr)
    var sum int
    for _, x := range xrr {
        var yi = sort.SearchInts(yrr,goal-x)
        if yi<len(yrr) {
            sum = x+yrr[yi]
            minAbs=minInt(minAbs,absInt(sum-goal))
        }
        if yi>0{
            sum = x+yrr[yi-1]
            minAbs=minInt(minAbs,absInt(sum-goal))
        }
    }
    return minAbs
}

func absInt(x int) int {
    if x > 0 {return x}
    return -x
}

func minInt(x, y int) int {
    if x < y {return x}
    return y
}

func subsetSums(nums []int, i int, sum int, subsets map[int]bool) {
    if i>=len(nums){
        subsets[sum]=true
        return
    }
    
    subsetSums(nums,i+1,sum+nums[i],subsets)
    subsetSums(nums,i+1,sum,subsets)
}

func flatten(mp map[int]bool) []int {
    var res []int
    for v, _ := range mp {
        res = append(res, v)
    }
    return res
}

func possible(val, target int) bool {
    return val >= target
}
