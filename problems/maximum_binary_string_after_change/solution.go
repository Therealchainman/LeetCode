func maximumBinaryString(binary string) string {
    n := len(binary)
    res := []rune(binary)
    for i, x := range binary {
        res[i] = x
    }
    var zeroStk []int
    for i, x := range binary {
        if x=='0' {
            zeroStk = append(zeroStk,i)
        }
    }
    leftZeros := false
    end := len(zeroStk)-1
    for i:=0;i<n;i++{
        if end<0 {
            break
        }
        if i > zeroStk[end] {
            break
        }
        if res[i]=='0'{
            leftZeros = true
        } else if res[i]=='1' && leftZeros {
            zI := zeroStk[end]
            end--
            res[zI] = '1'
            res[i]='0'
        }
    }
    for i:=1;i<n;i++ {
        if res[i-1]=='0' && res[i]=='0'  {
            res[i-1]='1'
        }
    }
    return string(res)
}