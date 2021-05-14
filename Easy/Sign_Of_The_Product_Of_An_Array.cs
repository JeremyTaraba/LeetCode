public class Solution {
    public int ArraySign(int[] nums) {
        
        int negSign = 0;
        
        foreach(int num in nums){
            if(num < 0){
                negSign++;
            }
            if(num == 0){
                return 0;
            }
            
        }
        
        if(negSign%2 == 0){
            return 1;
        }
        else{
            return -1;
        }
        
        
        
    }
}