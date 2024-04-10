class Solution {
    public int trap(int[] height) {
        // Can use extra memory O(n) although can be done in O(1)
        if(!(height.length > 2)){
            return 0;
        }
        int left = 0;
        int right = height.length-1;
        int maxLeft = height[0];
        int maxRight = height[height.length-1];
        int amount = 0;
        while(left <= right){
            if(maxLeft <= maxRight){
                if(maxLeft - height[left] > 0){
                    amount += maxLeft - height[left];
                    
                }
                if(maxLeft < height[left]){
                    maxLeft = height[left];
                }
               
                left++;
            }
            else{
                if(maxRight - height[right] > 0){
                    amount += maxRight - height[right];
                    
                }
                if(maxRight < height[right]){
                    maxRight = height[right];
                }
                right--;
            }
        }


        return amount;
    }
}