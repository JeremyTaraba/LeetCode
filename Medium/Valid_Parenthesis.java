class Solution {
    public boolean isValid(String s) {
        // order matters so we need to keep them in the same order
        // use stack to put half of the characters and then compare them with the other half
        // {([])}  [{,(,[,]
        
        if((s.length() & 1) != 0){
            return false;
        }  

        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{'){
                stack.push(s.charAt(i));
            }
            else if(s.charAt(i)==')' || s.charAt(i)=='}' || s.charAt(i)==']'){
                if(stack.isEmpty()){
                    return false;
                }
                if(stack.peek() == '(' && s.charAt(i) == ')'){
                    stack.pop();
                }
                else if(stack.peek() == '[' && s.charAt(i) == ']'){
                    stack.pop();
                }
                else if(stack.peek() == '{' && s.charAt(i) == '}'){
                    stack.pop();
                }
                else{
                    return false;
                }

            }
            
            
        }

        if(!stack.isEmpty()){
            return false;
        }

       

        return true;
    }
}