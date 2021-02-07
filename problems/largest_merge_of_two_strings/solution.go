func largestMerge(word1 string, word2 string) string {
    if len(word1)==0 || len(word2)==0 {
        return word1+word2
    }
    if word1 > word2 {
        return string(word1[0]) + largestMerge(word1[1:],word2)
    }
    return string(word2[0]) + largestMerge(word1,word2[1:])
}
