public class MyStack {

    Queue<int> Q1;
    Queue<int> temp;

    public MyStack() {
        Q1 = new Queue<int>();
        temp = new Queue<int>();
    }
    
    public void Push(int x) {
        Q1.Enqueue(x);
    }
    
    public int Pop() {
        int count = Q1.Count;
        temp.Clear();
        int val = -1;
        
        for(int i = 0; i < count; i++){
            if(i == count-1){
                val = Convert.ToInt32(Q1.Peek());
                Q1 = new Queue<int>(temp);               
                return val;
            }
            temp.Enqueue(Q1.Dequeue());
            
        }
        return -1;
    }
    
    public int Top() {
        int count = Q1.Count;
        int val = -1;
        temp = new Queue<int>(Q1);
        for(int i = 0; i < count; i++){
            if(i == count-1){
                val = Convert.ToInt32(temp.Peek());
                return val;
            }
            temp.Dequeue();
        }
        return -1;
    }
    
    public bool Empty() {
        return !Convert.ToBoolean(Q1.Count);
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * bool param_4 = obj.Empty();
 */