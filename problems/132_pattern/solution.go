func find132pattern(nums []int) bool {
    var n = len(nums)
    // You need at least 3 integers to have the 132 pattern.
    if n<3 {
        return false
    }
    var stack = []int{}
    var s1 = nums[n-1]
    var s3 int = -1e9
    for i:=n-2;i>=0;i-- {
        for len(stack)>0 && s1>stack[len(stack)-1] {
            s3=stack[len(stack)-1]
            stack=stack[:len(stack)-1]
        }
        stack=append(stack,s1)
        s1=nums[i]
        if s1<s3 {
            return true
        }
    }
    return false
}