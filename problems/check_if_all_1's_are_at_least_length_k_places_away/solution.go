func kLengthApart(nums []int, k int) bool {
    dist := 0
    seen := false
    for _, x := range nums {
        if x == 1 && seen && dist < k {
            return false
        }
        if x == 1 {
            dist = 0
            seen = true
        } else if x == 0 && seen {
            dist++
        }
    }
    return true
}