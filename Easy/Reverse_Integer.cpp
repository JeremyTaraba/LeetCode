
#include <limits.h>
using namespace std;

//first tried converting to string but difficult to check overflow so use int instead

class Solution {
public:
    int reverse(int x) {
       
      
        int number = 0;
        while(x != 0){
            int pop = x % 10;
            x = x / 10;
            if((number > INT_MAX/10) || (number == INT_MAX / 10 && pop > 7)){
                return 0;
            }
            if((number < INT_MIN/10) || (number == INT_MIN / 10 && pop < -8)){
                return 0;
            }
            number = number*10 + pop;
        }    
        
       
        return number;
    }
};