func champagneTower(poured int, query_row int, query_glass int) float64 {
    var cups = [101][101]float64{}
    cups[0][0] = float64(poured)
    for i :=0;i<100;i++ {
        for j := 0;j<=i;j++ {
            if cups[i][j]>=1 {
                var overflow = (cups[i][j]-1)/2.0
                cups[i+1][j]+=overflow
                cups[i+1][j+1]+=overflow
                cups[i][j]=1
            }
        }
    }
    return cups[query_row][query_glass]
}