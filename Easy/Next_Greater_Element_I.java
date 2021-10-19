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