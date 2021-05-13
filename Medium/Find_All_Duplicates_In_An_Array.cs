/*
Prompt:
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.s


*/



public class Solution {
    public IList<int> FindDuplicates(int[] nums) {
        HashSet<int> hSet = new HashSet<int>();
        List<int> ans = new List<int>();
        
        foreach(int i in nums){
            if(hSet.Contains(i)){
                ans.Add(i);
                continue;
            }
            hSet.Add(i);
        }
        
        return ans;
    }
}

/*
Notes:
Using hashset to check if we already added the int takes O(1) time or O(log n) in worst case
The foreach loop takes O(n) time

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.


*/