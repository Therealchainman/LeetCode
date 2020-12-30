type queue []int

func (arr *queue) Pop() int {
    old := (*arr)[0]
    (*arr)[0]=0
    *arr = (*arr)[1:];
    return old
}

func (arr *queue) Push(x int) {
    *arr = append(*arr, x)
}

func countStudents(students []int, sandwiches []int) int {
    cnt := 0
    sq := &queue{}
    saq := &queue{}
    for i:=0;i<len(students);i++ {
        *sq = append(*sq, students[i])
    }
    for i:=0;i<len(sandwiches);i++ {
        *saq = append(*saq, sandwiches[i])
    }
    for cnt<len(*sq) && len(*sq)>0 {
        if (*sq)[0]==(*saq)[0] {
            cnt = 0
            sq.Pop()
            saq.Pop()
        } else {
            cnt++
            s :=sq.Pop()
            sq.Push(s)
        }
    }
    return len(*sq)
}