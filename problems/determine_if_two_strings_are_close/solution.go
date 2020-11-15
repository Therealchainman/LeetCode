func helper(word string) map[rune]int {
    mp := make(map[rune]int)
    for _, c := range word {
        mp[c]++
    }
    return mp
}

func helper1(mp map[rune]int) map[int]int {
    cnt := make(map[int]int)
    for _, val := range mp {
        cnt[val]++
    }
    return cnt
}

func closeStrings(word1 string, word2 string) bool {
    if len(word1)!=len(word2) {
        return false
    }
    mp1:=helper(word1)
    mp2:=helper(word2)
    for key,_ := range mp1 {
        if _, found := mp2[key]; !found {
            return false
        }
    }
    for key,_ := range mp2 {
        if _, found := mp1[key]; !found {
            return false
        }
    }
    cnt1:=helper1(mp1)
    cnt2:=helper1(mp2)
    if len(cnt1)!=len(cnt2) {
        return false
    }
    eq := reflect.DeepEqual(cnt1,cnt2)
    return eq
}