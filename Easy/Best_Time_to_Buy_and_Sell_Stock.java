class Solution {
    public int maxProfit(int[] prices) {
        int lowestPrice = prices[0];
        int highestPrice = 0;
        int profit = 0;
        
        for(int i = 0; i < prices.length; i++){
            if(lowestPrice > prices[i]){
                lowestPrice = prices[i];
                highestPrice = 0;  //resets highest since we need a highest that is after lowest
            }
            if(highestPrice < prices[i]){
                highestPrice = prices[i];
            }
            if(highestPrice - lowestPrice > profit){    //incase lowest gets changed but the profit is not bigger
                profit = highestPrice - lowestPrice;
            }
            
        }
        
        
        if(profit > 0){
            return profit;
        }
        return 0;
    }
}