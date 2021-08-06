/*
Prompt: 
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:
 
abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

*/



public class Solution {
    public int MinDeletionSize(string[] strs) {
        int numDelete = 0;
        int columnLength = strs.Length;
        int rowLength = strs[0].Length;
        
        for(int i = 0; i < rowLength; i++){
            for(int j = 0; j < columnLength-1; j++){
                if(strs[j+1][i] < strs[j][i]){
                    numDelete++;
                    break;
                }
            }
        }
        
        return numDelete;
    }
}

/*
Notes:
Have to check the first letter of each columns and then the second letter of each column and so on
Make sure it is in descending order


Constraints:
n == strs.length
1 <= n <= 100
1 <= strs[i].length <= 1000
strs[i] consists of lowercase English letters.
 
*/
