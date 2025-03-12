public class Solution {
    public int MaxProfit(int[] prices) {
        // two pointer approach using left and right pointers
        
        int left = 0;
        int right = 1;
        int profit = 0;
        while (right < prices.Length){
            if(prices[left] < prices[right]){
                profit = Math.Max(profit, prices[right] - prices[left]);
            }
            else{
                left = right;
            }
            right++;
        }

        return profit;
    }
}