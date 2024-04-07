import java.util.Stack;

class Min_Stack {
    Stack<Integer> stack;
   Stack<Integer> minS;

   public Min_Stack() {
       stack = new Stack<>();
       minS = new Stack<>();
   }
   
   public void push(int val) {
       if(minS.isEmpty()){
           minS.push(val);
       }
       else if(minS.peek() >= val){
           minS.push(val);
       }
       stack.push(val);
       
   }
   
   public void pop() {
       if(stack.peek().intValue() == minS.peek().intValue()){
           stack.pop();
           minS.pop();
       }
       else{
           stack.pop();
       }
       
   }
   
   public int top() {
       return stack.peek();
   }
   
   public int getMin() {
       return minS.peek();
   }
}

/**
* Your MinStack object will be instantiated and called as such:
* MinStack obj = new MinStack();
* obj.push(val);
* obj.pop();
* int param_3 = obj.top();
* int param_4 = obj.getMin();
*/