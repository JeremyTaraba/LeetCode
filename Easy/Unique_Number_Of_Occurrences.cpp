/* 
Prompt:
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

*/



class Solution {
public:
    bool checkOccurrences(vector<int>& occur, int numOccur){
        for(int k = 0; k < occur.size(); k++){
                if(numOccur == occur.at(k)){
                    return false;   //occurs the same amount of time as something else
                }
            }
        return true;
    }
        
    bool uniqueOccurrences(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        arr.push_back(arr.at(arr.size()-1) + 1); //add a different value then the ending value
        vector<int> occurrences;
        int numOccur = 0;
        
        for(int i = 0; i < arr.size()-1; i++){
            if(arr.at(i) != arr.at(i+1)){
                numOccur++;
                if(!checkOccurrences(occurrences, numOccur)){
                    return false;
                }
                occurrences.push_back(numOccur);
                numOccur = 0;
            }
            else{
                numOccur++;
            }            
        }
        
        return true;
    }
};


/*
Notes:
Another approach is to sort the array and count the number of occurrences and put that into its own array. Then sort 
the new array and check to see if any numbers in this new array are the same


Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000


*/
