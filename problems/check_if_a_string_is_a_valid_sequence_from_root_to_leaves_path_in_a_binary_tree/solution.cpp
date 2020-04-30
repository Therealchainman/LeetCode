/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidSequence(TreeNode* root, vector<int>& arr) {
        int curr = 0;
        bool found = false;
        dfs(root, arr, curr, found);
        return found;
        
    }
    
    void dfs(TreeNode* root, vector<int>& arr, int& curr, bool& found) {
        if (!root || root->val != arr[curr]) {
            return;
        }
        if (!root->left && !root->right && arr.size() - 1 == curr) {
            found = true;
            return;
        }
        if (curr + 1 <= arr.size() - 1 && root->left) {
            dfs(root->left, arr, ++curr, found);
            curr--;
        }
        if (found) {
            return;
        }
        if (curr + 1 <= arr.size() - 1 && root->right) {
            dfs(root->right, arr, ++curr, found);
            curr--;
        }
        return;
    }
};