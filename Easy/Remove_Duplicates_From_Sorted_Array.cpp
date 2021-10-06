



class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        int j = 0;
        int nSize = nums.size();
        
        if(nSize == 0){
            return 0;
        } 
        
        for(j = 1; j < nSize; j++){
            if(nums.at(i) != nums.at(j)){
                i++;
                nums.at(i) = nums.at(j);
            }
        }
        return i + 1;
    }
};

/*
Notes:
Although this way is harder to visualize, it is much more efficient than if we checked to see if the elements next to each other were the same.
Instead we check to see if the elements are different and slide them down into the next space.


Constraints:
0 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.


*/