func check(B []int) bool {
    var mn = int(1e9)
    var x = -5
    var i = 0
    for i < len(B) {
        if B[i] <= mn {
            mn = B[i]
            x = i
        } 
        if i + 1 < len(B) && B[i+1]==mn && B[i] == mn {
            for i < len(B) && B[i] == mn {
                i++
            }
        } else {
            i++
        }

    }
    var A = make([]int, len(B))
    for i:=0;i<len(B);i++{
        A[i] = B[(i+x) % len(A)]
    }
    for i:=1;i<len(B);i++{
        if A[i-1]>A[i] {
            return false
        }
    }
    return true
}   