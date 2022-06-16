/*
Prompt:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

       
*/
    

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



/*
Notes:
Runtime is O(n) since only looping for n
We first find the lowest price, then we can find the highest price and sell. Can't do this the
other way around because we have to buy before we sell. Every time we change lowest we reset 
highest so that we dont sell before we buy.



Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104

*/
