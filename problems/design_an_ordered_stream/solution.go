type OrderedStream struct {
    ptr int
    stream map[int]string
}


func Constructor(n int) OrderedStream {
    
    return OrderedStream{
        ptr:  1,
        stream: make(map[int]string),
    }
}


func (this *OrderedStream) Insert(id int, value string) []string {
    this.stream[id]=value
    _, found := this.stream[this.ptr]
    var ret []string
    for found {
        ret=append(ret,this.stream[this.ptr])
        this.ptr++
        _, found = this.stream[this.ptr]
    }
    return ret
}


/**
 * Your OrderedStream object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Insert(id,value);
 */