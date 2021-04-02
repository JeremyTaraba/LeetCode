/*
Prompt:
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

Example:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

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
    int rangeSumBST(TreeNode* root, int low, int high) {
        if(root == NULL){
            return 0;
        }
        int sum = 0;
        if(root->val == high){
            //cout << "adding " << root->val << " to sum" << endl;
            sum+=root->val;
            return sum+=rangeSumBST(root->left, low, high);
        }
        else if(root->val > low){
            if(root->val < high){
                //cout << "adding " << root->val << " to sum" << endl;
                sum+=root->val;
            }
        }
        else if(root->val == low){
            //cout << "adding " << root->val << " to sum" << endl;
            sum+=root->val;
            return sum+=rangeSumBST(root->right, low, high);
        }
        else if(root->val < low){
            return sum+=rangeSumBST(root->right, low, high);
        }
        sum+=rangeSumBST(root->left, low, high);
        sum+=rangeSumBST(root->right, low, high);
        
        return sum;
    }
};

/*
Notes:
there are a lot of return statements within the if statements because I want to try to reduce how many nodes we search.
For example, if we know the current node is less than int low then we don't need to search any nodes left of that node.
BST is always sorted in order.

Constraints:
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

*/