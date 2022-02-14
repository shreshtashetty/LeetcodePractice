// 94. Binary Tree Inorder Traversal

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

vector<int> inorder(TreeNode* root, vector<int> l){
    
    if(root==nullptr){
        return l;
    }
    
    l = inorder(root->left, l);
    l.push_back(root->val);
    l = inorder(root->right, l);
    
    return l;
}

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> l;
        return inorder(root, l);
    }
};
