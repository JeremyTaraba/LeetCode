public class Solution {
    public string RemoveDuplicates(string S) {
        Stack<char> stack = new Stack<char>();
        
        
        foreach(char c in S){
            if(stack.Count > 0 && stack.Peek() == c){
                stack.Pop();
            }
            else{
                stack.Push(c);
            }
                
        }

        StringBuilder sb = new StringBuilder();
        while(stack.Count > 0){
            sb.Append(stack.Pop());
        }
        
        return new string(sb.ToString().Reverse().ToArray());
    }
}

/*
Notes:
Using a stack significantly reduces the run time as compared to using a loop to check the current and next character

Constraints:
1 <= S.length <= 20000
S consists only of English lowercase letters.

*/