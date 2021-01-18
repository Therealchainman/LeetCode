func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func maxOperations(nums []int, k int) int {
    freq := make(map[int]int)
    for _, x := range nums {
        freq[x]++
    }
    ans := 0
    for val, cnt := range freq {
        if val + val == k {
            ans += cnt/2
        } else if freq[k-val] > 0 {
            delta := min(cnt, freq[k-val])
            ans+=delta
            freq[k-val]-=delta
            freq[val]-=delta
        }
    }
    return ans
}