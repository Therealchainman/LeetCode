func isTransformable(w1, w2 string) bool {
    cnt := 0
    for i:=0;i<len(w1);i++ {
        if w1[i]!=w2[i] {
            cnt++
        }
    }
    return cnt==1
}
type w struct {
    level int
    word string
}
func bfs(b string, e string, A map[string][]string) int {
    var q []*w
    q = append(q, &w{1,b})
    visited := make(map[string]bool)
    for len(q)>0 {
        cur := q[0]
        curL := cur.level
        curW := cur.word
        if curW==e {
            return curL
        }
        q = q[1:]
        for _, x := range A[curW] {
            if !visited[x] {
                q = append(q, &w{curL+1,x})
                visited[x]=true
            }
            
        }
    }
    return 0
}
func ladderLength(beginWord string, endWord string, wordList []string) int {
    graph := make(map[string][]string)
    wordList = append(wordList, beginWord)
    n := len(wordList)
    for i:=0;i<n;i++ {
        for j:=0;j<n;j++ {
            if isTransformable(wordList[i],wordList[j]) {
                graph[wordList[i]] = append(graph[wordList[i]],wordList[j])
            }
        }
    }
    return bfs(beginWord,endWord,graph)
}