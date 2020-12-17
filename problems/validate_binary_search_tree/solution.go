/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func max(a, b int) int {
    if a>b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a<b {
        return a
    }
    return b
}

func treeTraversal(root *TreeNode, low int, high int) bool {
    if (root == nil) {
        return true;
    }
    if (root.Val)<=low || (root.Val)>=high {
        return false
    }
    uLow := max(low,root.Val)
    uHigh := min(high,root.Val)
    return treeTraversal(root.Left,low,uHigh) && treeTraversal(root.Right,uLow,high)
    
}
func isValidBST(root *TreeNode) bool {
    lo := -math.MaxInt64
    hi := math.MaxInt64
    return treeTraversal(root,lo,hi);
}