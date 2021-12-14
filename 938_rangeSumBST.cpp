// 938. Range Sum of BST

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
    int rangeSum(TreeNode* &root, int low, int high, int &sum){
        
        if(root==NULL){
            return sum;
        }

        if(root->val>=low && root->val<=high){
            sum+=root->val;
        }

        sum = rangeSum(root->left, low, high,sum);
        sum = rangeSum(root->right, low, high,sum);

        return sum;
    }
    
    int rangeSumBST(TreeNode* root, int low, int high) {
        int sum = 0;
        // cout<<(*root).left<<" "<<root->left;
        sum = rangeSum(root, low, high, sum);
        return sum;
    }
};
