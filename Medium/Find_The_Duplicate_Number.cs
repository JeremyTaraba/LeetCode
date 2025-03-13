public class Solution {
    public int FindDuplicate(int[] nums) {
        // floyds cycle finding (cannot use slow and fast pointer because it will go out of range)
        int slow = nums[0];
        int fast = nums[0];

        while (true){
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast){
                break;
            }
        }
        slow = nums[0];
        while (slow != fast){
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;

    }
}