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