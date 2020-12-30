func halvesAreAlike(s string) bool {
    vowels := make(map[byte]bool)
    vowels['a']=true
    vowels['A']=true
    vowels['e']=true
    vowels['E']=true
    vowels['I']=true
    vowels['i']=true
    vowels['u']=true
    vowels['U']=true
    vowels['o']=true
    vowels['O']=true
    cntLeft := 0
    cntRight := 0
    mid := len(s)/2
    for i:=0;i<mid;i++ {
        found, _ := vowels[s[i]]
        if found {
            cntLeft++
        }
    }
    for i:=mid;i<len(s);i++ {
        found, _ := vowels[s[i]]
        if found {
            cntRight++
        }
    }
    return cntLeft==cntRight
}