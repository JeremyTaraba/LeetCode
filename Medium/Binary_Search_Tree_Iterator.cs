/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class BSTIterator {
    int size = 0;
    int cur_pos = 0;
    List<int> list = new List<int>();

    public BSTIterator(TreeNode root) {
        cur_pos = 0;
        list = dfs(list,root);
        // foreach(int var in list){
        //     Console.WriteLine(var);
        // }
        size = list.Count();
    }

    private List<int> dfs(List<int> list, TreeNode root){
        if(root != null){
            list = dfs(list, root.left);
            list.Add(root.val);
            list = dfs(list, root.right);
        }
        return list;
    }

    
    public int Next() {
        cur_pos++;
        return list[cur_pos-1];
    }
    
    public bool HasNext() {
        return this.cur_pos < this.size;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.Next();
 * bool param_2 = obj.HasNext();
 */