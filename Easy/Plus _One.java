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