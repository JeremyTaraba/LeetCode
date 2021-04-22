/*
Prompt:
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.


Example:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.


*/


public class Solution {
    public int[] ReplaceElements(int[] arr) {
            int max = -1;
            int[] tempArr = new int[arr.Length];
            tempArr[arr.Length-1] = max;

            for (int i = arr.Length-1; i > 0; i--){
                if (arr[i] > max){
                    max = arr[i];
                }
                tempArr[i-1] = max;
            }

            return tempArr;
    }
}

/*
Notes:
Going through the array and looking for max from the back is faster than going through the array from the front for this problem

Constraints:
1 <= arr.length <= 104
1 <= arr[i] <= 105


*/