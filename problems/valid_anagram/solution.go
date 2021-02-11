func isAnagram(s string, t string) bool {
    var count = make(map[byte]int)
    if len(s)!=len(t){return false}
    for i, _ := range s {
        count[s[i]]++
        count[t[i]]--
    }
    for _, cnt := range count {
        if cnt > 0 {return false}
    }
    return true
}