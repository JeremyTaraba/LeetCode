class Solution {
    public boolean checkOccurrences(List<Integer> occur, int numOccur){
        for(int i = 0; i < occur.size(); i++){
            if(occur.get(i) == numOccur){
                return false;
            }
        }
        return true;
    }
    
    
    
    public boolean uniqueOccurrences(int[] arr) {
        List<Integer> occur = new ArrayList<Integer>();
        int numOccur = 0;
        Arrays.sort(arr);
        int[] tempArr = new int[arr.length + 1];
        System.arraycopy(arr, 0, tempArr, 0, arr.length);   //copy the original array to the new array
        tempArr[arr.length] = arr[arr.length - 1] + 1;
        
        for(int i = 0; i < tempArr.length - 1; i++){
            if(tempArr[i] != tempArr[i + 1]){
                if(!checkOccurrences(occur, numOccur)){
                    return false;
                }
                else{
                    occur.add(numOccur);
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
Notes:
Runtime is 1ms while the memory usage is 36.9mb
Faster than cpp which had 4ms runtime but much more memory than cpp 7.8mb


Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000


*/