/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func trimBST(root *TreeNode, low int, high int) *TreeNode {
    return walk(root, low, high)
}

func walk(root *TreeNode, low int, high int) *TreeNode {
    if root==nil {
        return nil
    }
    if root.Val<low {
        return walk(root.Right, low, high)
    } else if root.Val>high {
        return walk(root.Left, low, high)
    } else {
        root.Left = walk(root.Left, low, high)
        root.Right = walk(root.Right, low, high)
        return root
    }
}