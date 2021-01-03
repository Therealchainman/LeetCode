func min(x,y int) int {
    if x<y {
        return x
    }
    return y
}
func minMoves(nums []int, k int) int {
    if k==1 {
        return 0
    }
    n := len(nums)
    ans := 0
    var queue []int
    cntZeros := 0
    first := true
    for i:=0;i<n;i++ {
        if nums[i]==1 && first {
            first = false
            cntZeros=0
            continue
        }
        if nums[i]==1 {
            queue = append(queue,cntZeros)
            cntZeros = 0
        } else {
            cntZeros++
        }
    }
    n = len(queue)
    prefix := make([]int,n+1)
    for i:=1;i<n+1;i++ {
        prefix[i]=prefix[i-1]+queue[i-1]
    }
    radius := k/2
    leftSum:=0
    rightSum:=0
    if k%2!=0 {
        for i:=0;i<radius;i++{
            leftSum+=queue[i]*(i+1)
        }
        for i:=radius;i<radius*2;i++{
            rightSum+=queue[i]*(2*radius-i)
        }
        sum := leftSum+rightSum
        ans = sum
        for i:=radius;i<n-radius;i++ {
            deltaLeft := -(prefix[i]-prefix[i-radius])
            deltaRight := prefix[i+radius+1]-prefix[i+1]
            sum += deltaLeft + deltaRight
            ans = min(ans,sum)
        }
    } else {
        for i:=0;i<radius;i++{
            leftSum+=queue[i]*(i+1)
        }
        for i:=radius;i<radius*2-1;i++{
            rightSum+=queue[i]*(2*radius-i-1)
        }
        sum := leftSum+rightSum
        ans = sum
        for i:=radius;i<=n-radius;i++{
            deltaLeft := -(prefix[i]-prefix[i-radius])+queue[i]
            deltaRight := (prefix[i+radius]-prefix[i+1])
            sum += deltaLeft + deltaRight
            ans = min(ans,sum)
        }

    }
    return ans
}