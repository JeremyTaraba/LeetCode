/*
Prompt:
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


*/

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        boolean found = false;
        int curVal = 0;
        
        for(int i = 0; i < nums1.length; i++){
            curVal = nums1[i];
            nums1[i] = -1;
            found = false;
            
            for(int k = 0; k < nums2.length; k++){
                if(found && (nums2[k] > curVal) ){
                    nums1[i] = nums2[k];
                    break;
                }
                else if(nums2[k] == curVal){
                    found = true;
                }
            }
            
            
            
        }
        
        
        
        return nums1;
    }
}

/*
Notes:
O(n1 * n2)
There must be a more efficient way that is O(n1 + n2) will do more research

Constraints:
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.


*/