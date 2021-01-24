func diagonalSort(mat [][]int) [][]int {
    R := len(mat)
    C := len(mat[0])
    diagonalMap := make(map[int][]int)
    for r:=0;r<R;r++ {
        for c:=0;c<C;c++ {
            diagonalMap[r-c] = append(diagonalMap[r-c],mat[r][c])
        }
    }
    for _, v := range diagonalMap {
        sort.Ints(v)
    }
    for r:=0;r<R;r++ {
        for c:=0;c<C;c++ {
            mat[r][c] = diagonalMap[r-c][0]
            diagonalMap[r-c] = diagonalMap[r-c][1:]
        }
    }
    return mat
}