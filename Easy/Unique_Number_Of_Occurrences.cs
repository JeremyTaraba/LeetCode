/*
Prompt:
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.


*/


public class Solution {
    public bool NumOccurrences(List<int> occur, int numOccur){
        foreach(int i in occur){
            if(i == numOccur){
                return false;
            }
        }
        
        return true;
    }
    
    
    public bool UniqueOccurrences(int[] arr) {
        List<int> occur = new List<int>();
        int numOccur = 0;
        Array.Sort(arr);
        
        int[] tempArr = new int[arr.Length + 1];
        arr.CopyTo(tempArr, 0);
        tempArr[arr.Length] = arr[arr.Length - 1] + 1;
        
        for(int i = 0; i < tempArr.Length-1; i++) {
            if(tempArr[i] != tempArr[i+1]){
                if(!NumOccurrences(occur, numOccur)){
                    return false;
                }
                else{
                    occur.Add(numOccur);
                    numOccur = 0;
                }
            }
            else{
                numOccur++;
            }
        }
        
        return true;
    }
}

/*
Note:
Can't use foreach as the main loop since we need the current and next array element.
As a side note, running this in cpp gives a runtime of 4ms and 7.8mb of memory while running in c# gives 92ms and 24.7mb of memory.
Can defininitely optimize the c# code to be faster but not as fast as the cpp code.

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

*/