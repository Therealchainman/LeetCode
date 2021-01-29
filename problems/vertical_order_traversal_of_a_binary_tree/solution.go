/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type prop struct {
    x int
    y int 
    node *TreeNode
}

func verticalTraversal(root *TreeNode) [][]int {
    var q []prop
    var a []prop
    q = append(q, prop{0,0,root})
    for len(q) > 0 {
        node := q[len(q)-1]
        a = append(a, node)
        q = q[:len(q)-1]
        if node.node.Left != nil {
            q = append(q, prop{node.x-1,node.y-1,node.node.Left})
        }
        if node.node.Right != nil {
            q = append(q, prop{node.x+1,node.y-1,node.node.Right})
        }
    }
    sort.SliceStable(a, func(i, j int) bool {
        if a[i].x != a[j].x {
            return a[i].x < a[j].x
        } else if a[i].y != a[j].y {
            return a[i].y > a[j].y
        } else {
            return a[i].node.Val < a[j].node.Val
        }
    })
    prevX := -int(1e9)
    var ans [][]int
    for _, p := range a {
        if p.x != prevX {
            ans = append(ans, []int{p.node.Val})
            prevX = p.x
        } else {
            ans[len(ans)-1] = append(ans[len(ans)-1], p.node.Val)
        }
    }
    return ans
}