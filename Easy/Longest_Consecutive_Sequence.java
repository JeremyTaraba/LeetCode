import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        int ans = 0;
        Set<Integer> numSet = new HashSet<Integer>();
        for(int num: nums){
            numSet.add(num);
        }
         for(Integer i: numSet){
            //check for start of set
            if(!numSet.contains(i-1)){
                int tempAns = 1;
                while(numSet.contains(i+tempAns)){
                    tempAns++;
                }
                if(ans < tempAns){
                    ans = tempAns;
                }
            }
        }

        return ans;
    }
}