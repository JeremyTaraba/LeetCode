#include <math.h>

class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;
        int temp = 0;
        int j = 0;
        
        for(int i = 5; i >= 0; i--){
            temp = n / pow(10,i);
            if(temp != 0){
                j = i;
                break;
            }
        }
        
        for(int i = j; i >= 0; i--){
            temp = n / pow(10,i);
            product = product * temp;
            sum = sum + temp;
            n = n - temp * pow(10,i);
        }
        
        
        
        
        
        return product - sum;
    }
};