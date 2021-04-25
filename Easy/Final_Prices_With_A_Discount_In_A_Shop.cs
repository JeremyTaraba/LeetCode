public class Solution {
    public int[] FinalPrices(int[] prices) {
        
        for(int i = 0; i < prices.Length - 1; i++){
            for(int j = i + 1; j < prices.Length; j++){
                if(prices[i] - prices[j] >= 0){
                    prices[i] = prices[i] - prices[j];
                    break;
                }
            }
        }
        
        return prices;
    }
}

/*
Notes:
Might be a way to reduce the runtime a little bit by skipping the values which can't be reduced further


Constraints:
1 <= prices.length <= 500
1 <= prices[i] <= 10^3

*/