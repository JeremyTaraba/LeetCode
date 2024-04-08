import java.util.ArrayList;
import java.util.*;

public class Generate_Parenthesis {

    public void backtracking(List<String> ans, int open, int close, int n, String str) {
        if(str.length() == n*2){
            ans.add(str);
            return;
        }
        if(open < n){
            backtracking(ans, open+1, close, n, str+"(");
        }
        if(close < open){
            backtracking(ans, open, close+1, n, str+")");
        }
    }
    
    public List<String> generateParenthesis(int n) {
        // backtracking since we need all combinations

        List<String> ans = new ArrayList<>();
        backtracking(ans,0,0,n,"");
        
        return ans;
    }
}
