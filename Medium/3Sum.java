class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // can create a map of all nums so finding them is O(1)
        // can pick 1 num and pick another num and then see if num exists in map that makes them 0 --> O(n^2)
        // backtracking would take O(v^2)

        Arrays.sort(nums); // O(n log n)
       
        List<List<Integer>> ans = new ArrayList<>();
        int target = 0;
        int left = 0;
        int right = nums.length-1;
        List<Integer> singleAns = new ArrayList<>();
        for(int i = 0; i < nums.length-2; i++){
             if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            singleAns = new ArrayList<>();
            target = nums[i];
            left = i+1;
            right = nums.length - 1;
            while(left < right){
               
                if(nums[left] + nums[right] + target == 0){
                    singleAns.add(target);
                    singleAns.add(nums[left]);
                    singleAns.add(nums[right]);
                    ans.add(singleAns);
                    singleAns = new ArrayList<>();

                    while(left < right && nums[left] == nums[left+1]){
                        left++;
                    }
                    while(left < right && nums[right] == nums[right-1]){
                        right--;
                    }
                    left++;
                    right--;
                    
                   
                }
                else if(nums[left] + nums[right] + target < 0){
                    left++;
                }
                else{
                    right--;
                }
                
                
            }
            
        }
        return ans;

    }
}
