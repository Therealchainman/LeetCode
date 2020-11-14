func mod(a int, b int) int {
    return (a%b + b)%b
}
func decrypt(code []int, k int) []int {
    ret := []int{}
    if k==0 {
        for i:=0;i<len(code);i++ {
            ret=append(ret,0)
        }
        return ret
    }
    if k>0 {
        s := 0
        for i:=1;i<=k;i++ {
            s+=code[i]
        }
        for i:=0;i<len(code);i++ {
            ret=append(ret,s)
            s-=code[mod(i+1,len(code))]
            s+=code[mod(i+k+1,len(code))]
        }
        return ret
    }
    if k<0 {
        s:=0
        for i:=len(code)-1;i>=len(code)+k;i-- {
            s+=code[i]
        }
        for i:=0;i<len(code);i++ {
            ret=append(ret,s)
            s-=code[mod(i+k,len(code))]
            s+=code[i]
        }
        return ret
    }
    return ret
}