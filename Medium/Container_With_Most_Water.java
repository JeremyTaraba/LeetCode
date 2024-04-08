class Solution {
    public int maxArea(int[] height) {
        // brute force is O(n^2) to check every combination
        // optimal is O(n) where you use left and right

        int left = 0;
        int right = height.length-1;
        int maxArea = 0;
        while(left < right){
            if (maxArea < ( (right - left) * Math.min(height[right],height[left]) )){
                maxArea = (right - left) * Math.min(height[right],height[left]);
               
            }
            if(height[left] < height[right]){
                left++;
            }
            else if(height[left] > height[right]){
                right--;
            }
            else{
                if(height[left+1] < height[right-1]){
                    right--;
                }
                else if(height[left+1] > height[right-1]){
                    left++;
                }
                else{
                    left++;
                }
            }
            
        }


        return maxArea;
    }
}