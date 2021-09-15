//     int maxDepth(TreeNode* root) {
//         if(root == NULL){
//             return 0;
//         }
//         int depth = 0;
//         return maxDepthFinder(root, depth);
//     }
    
//     int maxDepthFinder(TreeNode* root, int depth){
//         depth +=1;
//         if(root->left == NULL && root->right == NULL){  
//             return depth;
//         }
//         if(root->right == NULL){
//             return maxDepthFinder(root->left, depth);
//         }
//         if(root->left == NULL){
//             return maxDepthFinder(root->right, depth);
//         }
//         int right;
//         int left;
//         right = maxDepthFinder(root->right, depth);
//         left = maxDepthFinder(root->left, depth);
        
//        return max(left,right);
        
//     }
    
    int maxDepth(TreeNode* root) {

        if(root == NULL){
            return 0;
        }
        
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }


/*
Notes:
Commented out solution has a runtime 4* longer than the second solution. 
The first solution is better for adding up values within the nodes. For finding the depth we don't need
to make it so complicated

Contraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

*/