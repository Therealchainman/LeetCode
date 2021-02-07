
func sumOfUnique(nums []int) int {
    var count = make(map[int]int)
    var res = 0
    for _, num := range nums{
        count[num]++
    }
    for val, cnt := range count{
        if cnt==1{
            res+=val
        }
    }
    return res
}