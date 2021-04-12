/*
Prompt:
Given the root of a binary tree, return the sum of values of its deepest leaves.

*/



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
     int getDepth(TreeNode* root) { //returns depth where root = 1
        if (root == NULL){
            return 0;
        }
        int leftDepth = getDepth(root->left);
        int rightDepth = getDepth(root->right);
         
        if (leftDepth > rightDepth){
            return(leftDepth + 1);
        }
        else {
            return(rightDepth + 1);
        }
    }
    
    int Sum(TreeNode* root, int depth, int currDepth) {
        if (root == NULL){
            return 0;
        } 
        //cout << "depth = " << depth << endl;
        int sum = 0;
        if (currDepth == depth){ 
            return root->val;
        }
        sum+=Sum(root->left, depth, currDepth + 1); 
        sum+=Sum(root->right, depth, currDepth + 1);
        return sum;
    }
    
    int deepestLeavesSum(TreeNode* root) {
        int depth = getDepth(root);
        int sum = Sum(root, depth-1, 0);
        return sum;
        
    }
};


/*
Notes:




*/