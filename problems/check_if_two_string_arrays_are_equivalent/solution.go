func arrayStringsAreEqual(word1 []string, word2 []string) bool {
    var str1 strings.Builder
    var str2 strings.Builder
    for _, w := range word1 {
        str1.WriteString(w)
    }
    for _, w := range word2 {
        str2.WriteString(w)
    }
    return str1.String()==str2.String()
}