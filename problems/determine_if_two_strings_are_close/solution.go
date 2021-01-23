func setCharCountWord(word string) map[rune]int {
    charCountMap := make(map[rune]int)
    for _, ch := range word {
        charCountMap[ch]++
    }
    return charCountMap
}

func setFreq(charMap map[rune]int) map[int]int {
    freq := make(map[int]int)
    for _, cnt := range charMap {
        freq[cnt]++
    }
    return freq
}

func closeStrings(word1 string, word2 string) bool {
    charCountWord1 := setCharCountWord(word1)
    charCountWord2 := setCharCountWord(word2)
    for ch, _ := range charCountWord1 {
        if _, found := charCountWord2[ch]; !found {
            return false
        }
    }
    for ch, _ := range charCountWord2 {
        if _, found := charCountWord1[ch]; !found {
            return false
        }
    }
    freqWord1 := setFreq(charCountWord1)
    freqWord2 := setFreq(charCountWord2)
    eq := reflect.DeepEqual(freqWord1, freqWord2)
    return eq
}