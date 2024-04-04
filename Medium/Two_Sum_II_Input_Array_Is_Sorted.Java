class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // already sorted, can use binary search can go through array in O(n) time and use binary search to find other num
        // will take O(n log n) with O(1) space
        // can put them in a map O(n) extra space and time and then go through array in n time and check if num in map O(1)
        // would be O(n) time with O(n) space ***solution must use constant space so we cant do this
       

        //[1,2,3,4,5] targ = 3

        int[] ans = new int[2];
        
        int left = 0; // space we already searched
        int right = numbers.length-1;   // space need to search
        int newTarget = 0;
        int mid = left + (right - left) / 2;
        for(int i = 0; i < numbers.length; i++){
            left = i+1;
            right = numbers.length-1;
            newTarget = target - numbers[i];
            while(left <= right){
                mid = left + (right - left) / 2;
                if(numbers[mid] == newTarget){
                    ans[0] = i + 1;
                    ans[1] = mid + 1;
                    return ans;
                }
                else if(numbers[mid] < newTarget){
                    left = mid + 1;
                }
                else{
                    right = mid - 1;
                }
            }

        }
        





        return ans;
    }
}