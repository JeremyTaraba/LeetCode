import static java.lang.Math.*;

class Solution {
    public int[] plusOne(int[] digits) {
        
        
        int lastDigit = digits[digits.length - 1];
        if(lastDigit != 9){
            lastDigit += 1;
            digits[digits.length - 1] = lastDigit;
        }
        else{
            int curIndex = digits.length - 1;
            int curDigit = digits[curIndex];
            
            while(curDigit == 9){
                if(curIndex == 0){
                    int[] answer = new int[digits.length+1];
                    answer[0] = 1;  //in java int arrays initialize as 0 so only change first number
                    return answer;
                }
                else{
                    curIndex--;
                    curDigit = digits[curIndex];
                    
                    if(curDigit != 9){
                        digits[curIndex] = curDigit + 1;
                        for(int i = curIndex+1; i < digits.length; i++){
                            digits[i] = 0;
                        }
                    }
                    
                }
                
            }
        }
        
        
        
        return digits;
    }
}

/*
Notes:
First attempt at this was to convert the int array to an int and add one then convert back into an array.
This does not work with numbers larger than max_int. Solution is to either convert it into an unsigned long but that would just increase the limit.
Instead, I made it so the size of the number does not matter.


Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

*/