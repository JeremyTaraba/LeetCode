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

