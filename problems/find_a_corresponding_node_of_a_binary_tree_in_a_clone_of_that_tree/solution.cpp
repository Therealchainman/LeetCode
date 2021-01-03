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
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        stack<pair<TreeNode*,TreeNode*>> stk;
        stk.emplace(original,cloned);
        TreeNode* curOrig;
        TreeNode* curCloned;
        while (!stk.empty()) {
            tie(curOrig,curCloned) = stk.top();
            stk.pop();
            if (curOrig==target) {
                return curCloned;
            }
            if (curOrig->left != nullptr) {
                stk.emplace(curOrig->left,curCloned->left);
            } 
            if (curOrig->right != nullptr) {
                stk.emplace(curOrig->right,curCloned->right);
            }
        }
        return curCloned;
    }
};