/*
Prompt:
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.


*/



class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int largestValue = candies.at(0);
        int largestIndex;
        vector<bool> output;
        
        //find largest value
        for(int i = 0; i < candies.size(); i++){
            if(largestValue < candies.at(i)){
                largestValue = candies.at(i);
            }
        }
        
        //see if extra candies can be greater than or equal to largest value
        for(int i = 0; i < candies.size(); i++){
            if( (candies.at(i) + extraCandies) >= largestValue){
                output.push_back(true);
            }
            else{
                output.push_back(false);
            }
        }
        
        return output;
    }
};

/*
This solution seems to have the fastest run time. Memory usage wise, it could be better by using smaller data types. 
candies can only be numbers 1-100 so we dont need negative values and we don't need more than 256 numbers.

*/