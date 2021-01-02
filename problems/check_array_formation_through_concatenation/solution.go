func canFormArray(arr []int, pieces [][]int) bool {
    n := len(arr)
    m := len(pieces)
    pMap := make(map[int]int)
    for j:=0;j<m;j++ {
        pMap[pieces[j][0]]=j
    }
    i := 0
    for i < n {
        index, found := pMap[arr[i]]
        if found {
            for j:=0;j<len(pieces[index]);j++ {
                if pieces[index][j]!=arr[i] {
                    return false
                }
                i++
            }
        } else {
            return false
        }
    }
    return true
}