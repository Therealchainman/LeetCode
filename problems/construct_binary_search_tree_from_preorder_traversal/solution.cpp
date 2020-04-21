/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        if (preorder[0] == 0) {
            return NULL;
        }
        if (preorder.size() == 1) {
            return new TreeNode(preorder[0]);
        } 
        int leftIndex = 0; int rightIndex = 0; int rootIndex = 0;
        for (int i = 1; i < preorder.size(); i++) {
            if (preorder[i] > preorder[rootIndex]) {
                rightIndex = i;
                break;
            }
        }
        for (int i = 1; i < preorder.size(); i++) {
            if (preorder[i] < preorder[rootIndex]) {
                leftIndex = i;
                break;
            }
        }
        vector<int> rightSubtree(preorder.cbegin() + rightIndex, preorder.cend());
        vector<int> leftSubtree(preorder.cbegin() + 1, (rightIndex != 0) ? (preorder.cbegin() + rightIndex) : preorder.cend());
        if (rightIndex == 0) {
            rightSubtree = {0};
        }
        if (leftIndex == 0) {
            leftSubtree = {0};
        }
        TreeNode* node = new TreeNode(preorder[0]);
        if (rightSubtree[0] != 0) {
            node->right = bstFromPreorder(rightSubtree);
        }
        if (leftSubtree[0] != 0) {
            node->left = bstFromPreorder(leftSubtree);
        }
        return node;
    }
};