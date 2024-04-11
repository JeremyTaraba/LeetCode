class Solution {
    public int evalRPN(String[] tokens) {
        // when we see an operator we pop off two numbers from the stack
        Stack<String> numbers = new Stack<>();
        Set<String> set = new HashSet<String>(); 
        set.add("+");
        set.add("-");
        set.add("*");
        set.add("/");

        for(String num : tokens){
            if(set.contains(num)){
                String a = numbers.pop();
                String b = numbers.pop();
                int result = 0;
                switch (num){
                    case "+":
                        result = (Integer.parseInt(b) + Integer.parseInt(a));
                        break;
                    case "-":
                        result = (Integer.parseInt(b) - Integer.parseInt(a));
                        break;
                    case "*":
                        result = (Integer.parseInt(b) * Integer.parseInt(a));
                        break;
                    case "/":
                        if(Integer.parseInt(b) < 0 ^  Integer.parseInt(a) < 0){
                            result = Math.floorDiv(Integer.parseInt(b) * -1, Integer.parseInt(a));
                            result *= -1;
                        }
                        else{
                            result = Math.floorDiv(Integer.parseInt(b), Integer.parseInt(a));
                        }
                        
                       
                        break;
                }
                numbers.push(String.valueOf(result));
            }
            else{
                numbers.push(num);
            }
        }
        return Integer.parseInt(numbers.pop());
    }
}