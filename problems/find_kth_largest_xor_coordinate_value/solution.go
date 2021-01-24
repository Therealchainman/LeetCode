func kthLargestValue(matrix [][]int, k int) int {
    R := len(matrix)
    C := len(matrix[0])
    mat := make([][]int,R)
    for i, c := range mat {
        c = make([]int,C)
        mat[i]=c
    }
    for c:=0;c<C;c++ {
        row := 0
        for r:=0;r<R;r++ {
            row^=matrix[r][c]
            mat[r][c]=row
        } 
    }
    var ans []int
    for r:=0;r<R;r++ {
        col := 0
        for c:=0;c<C;c++ {
            col^=mat[r][c]
            ans = append(ans, col)
        }
    }
    sort.SliceStable(ans, func(i, j int) bool {
        return ans[i] > ans[j]
    })
    return ans[k-1]
}