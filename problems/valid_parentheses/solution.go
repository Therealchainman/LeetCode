func isValid(s string) bool {
    var stk []byte
    parens := map[byte]byte{
        ']':'[',
        ')':'(',
        '}':'{',
    }
    for _, c := range s {
        ch := byte(c)
        if ch == '[' || ch=='{' || ch=='(' {
            stk = append(stk, ch)
        } else {
            if len(stk)==0 {
                return false
            }
            opened := stk[len(stk)-1]
            if parens[ch]!=opened {
                return false
            }
            stk = stk[:len(stk)-1]
        }
    }
    return len(stk)==0
}