#include <iostream>
using namespace std;

//counting how many bits are different from two decimal numbers
//returning that as the distance
//is there a better way to do this? maybe there is a formula to calculate the bit difference
//without having to convert it into binary
//do research into this

class Solution {
public:

    int hammingDistance(int x, int y) {
        int binaryArrayX[32] = {0};
        int binaryArrayY[32] = {0};
        int i = 0;
        int hammingDistance = 0;
        
        while(x > 0){
            binaryArrayX[i] = x % 2; 
            x = x / 2; 
            i++; 
        }
        i = 0;
        while(y > 0){
            binaryArrayY[i] = y % 2; 
            y = y / 2; 
            i++; 
        }
        
   
        for (int j = 31; j >= 0; j--) {  //don't have to reverse this but easier to visualize what is going on
            if(binaryArrayX[j] != binaryArrayY[j] ){
                hammingDistance++;
            }
          
        }
        
        return hammingDistance;
    }
    
};