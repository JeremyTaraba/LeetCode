class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if(nums1.empty()){
            nums1 = nums2;
            return;
        }
        if(nums2.empty()){
            return;
        }
        //remove trailing zeros
        vector<int>::iterator it = nums1.end()-1;  
        for(int i = 0; i < n; i++){
            nums1.erase(it);
            it--;
        }
        
        //insert nums2 into correct position
        vector<int>::iterator counter = nums1.begin();
        while(!nums2.empty()){
            if(*counter > nums2.at(0)){
                nums1.insert(counter, nums2.at(0));
                nums2.erase(nums2.begin()); //after inserting, delete begining of nums2
            }
            if(counter == nums1.end()){
                nums1.push_back(nums2.at(0));
                nums2.erase(nums2.begin());
            }
            else{
                counter++;
            }
        }
        
    }
};