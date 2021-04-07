/*
Prompt:
Design a stack which supports the following operations.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, just increment all the elements in the stack.

*/



class CustomStack {
private:
    vector<int> stackType;
    
public:
    int max = -1;
    int top = -1;
    
    CustomStack(int maxSize) {
        max = maxSize;
    }
    
    void push(int x) {
        if(top >= (max-1)){
            return;
        }
        top++;
        stackType.push_back(x);
    }
    
    int pop() {
        if(top < 0){
            return -1;
        }
        int value = stackType.at(top);
        stackType.pop_back();
        top--;
        return value;
    }
    
    void increment(int k, int val) {
        if(k > top){
            k = top + 1;
        }
        for(int i = 0; i < k; i++){
            stackType.at(i) += val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */



/*
Notes
Could use an array of ints instead of a vector<int> if size is a problem but using a vector is just easier to code


Constraints:
1 <= maxSize <= 1000
1 <= x <= 1000
1 <= k <= 1000
0 <= val <= 100
At most 1000 calls will be made to each method of increment, push and pop each separately

*/