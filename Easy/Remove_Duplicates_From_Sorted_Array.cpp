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



Constraints:



*/