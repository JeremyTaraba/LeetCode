/*
Prompt:
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i]


Example:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
*/


class Solution {
public:
    
    int partition(vector<int> &values, int left, int right) {   //recursive function for swapping values around
        int pivotIndex = left + (right - left) / 2; //finding the middle index; left and right are indices
        int pivotValue = values[pivotIndex];    //finding the middle value
        int i = left, j = right;    
        int temp;
        while(i <= j) {
            while(values[i] < pivotValue) {
                i++;
            }
            while(values[j] > pivotValue) {
                j--;
            }
            if(i <= j) {
                temp = values[i];
                values[i] = values[j];
                values[j] = temp;
                i++;
                j--;
            }
        }
        return i;
    }
    
    void quicksort(vector<int> &values, int left, int right) {
        if(left < right) {
            int pivotIndex = partition(values, left, right);
            quicksort(values, left, pivotIndex - 1);
            quicksort(values, pivotIndex, right);
        }
    }
    
    
    
    int heightChecker(vector<int>& heights) {
        int wrongHeights = 0;
        vector<int> expected = heights;
        quicksort(expected, 0, expected.size()-1);
        
        for(int i = 0; i < expected.size(); i++){
            if(expected.at(i) != heights.at(i)){
                wrongHeights++;
            }
        }
        
        return wrongHeights;
    }
};

/*
Notes:
I don't think there is any way to get around having to sort the vector. 
Instead of writing a quicksort you could also use the built in sort function for vectors

Constraints:
1 <= heights.length <= 100
1 <= heights[i] <= 100


*/