func canPlaceFlowers(flowerbed []int, n int) bool {
    flowerbed = append([]int{0},flowerbed...)
    flowerbed = append(flowerbed,0)
    for i:=1;i<len(flowerbed)-1;i++ {
        if flowerbed[i]==1 {
            continue
        }
        if flowerbed[i-1]+flowerbed[i+1] == 0 {
            flowerbed[i]=1
            n--
        }
    }
    return n<=0
}