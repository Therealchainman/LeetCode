/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

type object struct {
    node *Node
    depth int
}

func connect(root *Node) *Node {
    if root == nil {
        return root
    }
    queue := []object{object{node: root, depth: 0}}
    prevNode := &Node{}
    prevDepth := 0
    for len(queue)>0 {
        curNode := queue[0].node
        curDepth := queue[0].depth
        queue[0]=object{}
        queue = queue[1:]
        if prevDepth == curDepth {
            prevNode.Next = curNode
        }
        if curNode.Left != nil {
            queue = append(queue, object{node: curNode.Left, depth: curDepth+1})
        }
        if curNode.Right != nil {
            queue = append(queue, object{node: curNode.Right, depth: curDepth+1})
        }
        prevNode = curNode
        prevDepth = curDepth
    }
    return root
}