/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        maxSoFar(root);
        return max;
    }
    private int maxSoFar(TreeNode root) {
        if (root == null) {
            return 0;
        }
        
        int leftMax = maxSoFar(root.left);
        int rightMax = maxSoFar(root.right);
        
        int ret = Math.max(root.val, Math.max(root.val + leftMax, root.val + rightMax));
        max = Math.max(max, leftMax + root.val + rightMax);
        
        return ret > 0 ? ret : 0;
    }
}