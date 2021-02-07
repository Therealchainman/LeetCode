/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */


type input struct{
    Node *TreeNode
    Level int
}
func rightSideView(root *TreeNode) []int {
    var ans []int
    if root==nil {
        return ans
    }
    var q = []input{input{root,1}}
    for len(q)>0{
        var cur = q[0]
        q = q[1:]
        if len(ans)<cur.Level{
            ans = append(ans, cur.Node.Val)
        }
        if cur.Node.Right!=nil{
            q=append(q,input{cur.Node.Right,cur.Level+1})
        }
        if cur.Node.Left!=nil{
            q=append(q,input{cur.Node.Left,cur.Level+1})
        }
    }
    return ans
}