import java.util.HashMap;
import java.util.Map;

class Solution {    // put nums into a map and save index and then check for remained after subtracting the target
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> myMap = new HashMap<>();
        int n = nums.length;

        
        for (int i = 0; i < n; i++) {
            myMap.put(nums[i], i);
        }

       
        for (int i = 0; i < n; i++) {
            int remainder = target - nums[i];
            if (myMap.containsKey(remainder) && myMap.get(remainder) != i) {
                return new int[]{i, myMap.get(remainder)};
            }
        }

        return new int[]{}; // No solution found
    }
}