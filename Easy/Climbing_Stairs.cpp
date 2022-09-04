class Solution {
public:
    int climbStairs(int n) {
        int first = 1;
        int second = 1;
        int start = 2;
        int temp = 0;
        if(n == 1){
            return 1;
        }
        if(n == 2){
            return 2;
        }
        for(int i = 2; i < n; i++){
            start = start + second;
            temp = first;
            first = second;
            second = temp + second;
            
            
        }
        
        return start;
    }
};