class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int value = 0;
        for(String x:operations){
            if(x.charAt(1) == '+'){
                value++;
            }
            else{
                value--;
            }
        }
        
        return value;
    }
}