/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    var front = head
    var copy = make(map[*Node]*Node)
    for front!=nil {
        copy[front]=&Node{front.Val,nil,nil}
        front=front.Next
    }
    front = head
    for front!=nil{
        copy[front].Next=copy[front.Next]
        copy[front].Random=copy[front.Random]
        front=front.Next
    }
    return copy[head]
}