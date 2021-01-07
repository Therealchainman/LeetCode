func findKthPositive(arr []int, k int) int {
    i:=0
    num:=1
    for true {
        if i<len(arr) && arr[i]==num {
            i++
        } else {
            k--
        }
        if k==0 {
            break
        }
        num++
    }
    return num
}