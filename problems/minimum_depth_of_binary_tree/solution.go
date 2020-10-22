/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeLoc struct {
    Node *TreeNode
    Depth int
}

func minDepth(root *TreeNode) int {
    if root == nil {
        return 0
    }
    var queue []TreeLoc
    queue=append(queue,TreeLoc{Node:root,Depth:1})
    for len(queue)>0 {
        var node = queue[0]
        if node.Node.Left == nil && node.Node.Right == nil {
            return node.Depth
        }
        queue=queue[1:]
        if node.Node.Left != nil {
            queue=append(queue,TreeLoc{Node:node.Node.Left,Depth:node.Depth+1})
        }
        if node.Node.Right != nil {
            queue=append(queue,TreeLoc{Node:node.Node.Right,Depth:node.Depth+1})
        }
    }
    return 0
}