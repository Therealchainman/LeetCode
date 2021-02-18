func maxArea(height []int) int {
    n:=len(height)
    left, right, best := 0,n-1, 0
    var curHeight int
    for left<right {
        curHeight = min(height[left],height[right])
        best=max(curHeight*(right-left),best)
        if height[right]>height[left]{
            left++
        } else {
            right--
        }
    }
    return best
}

func max(x, y int) int {
    if x > y {return x}
    return y
}
func min(x, y int) int {
    if x < y {return x}
    return y
}

