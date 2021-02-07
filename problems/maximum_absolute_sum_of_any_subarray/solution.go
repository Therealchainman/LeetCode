func maxAbsoluteSum(nums []int) int {
    var maxVal = 0
    var sumPos = 0
    var sumNeg = 0
    for _, n := range nums {
        sumPos+=n
        sumNeg+=n
        if sumPos<0 {
            sumPos=0
        }
        if sumNeg > 0{
            sumNeg=0
        }
        maxVal = max(maxVal,sumPos)
        maxVal = max(maxVal,-sumNeg)
    }
    return maxVal
}

func max(x ,y int) int {
    if x > y {return x}
    return y
}