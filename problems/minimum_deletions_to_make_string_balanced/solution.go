func minimumDeletions(s string) int {
    ret := 0
    var stk []byte
    for i:=len(s)-1;i>=0;i-- {
        if len(stk)>0 && stk[len(stk)-1]<s[i] {
            ret++
            stk[len(stk)-1]=0
            stk=stk[:len(stk)-1]
        } else {
            stk=append(stk,s[i])
        }
    }
    return ret
}