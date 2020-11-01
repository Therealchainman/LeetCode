func canFormArray(arr []int, pieces [][]int) bool {
    // The idea is to form a map that maps element -> index. 
    mp := make(map[int]int)
    for i,p := range pieces {
        mp[p[0]]=i;
    }
    var i = 0
    for i<len(arr) {
        if index, found := mp[arr[i]]; found {
            for _,elem := range pieces[index] {
                if arr[i]!=elem {
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