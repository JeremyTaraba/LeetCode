class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // min eating speed will be total bananas / hours  rounded up
        int max = piles[0];
        for(int num : piles){
            if(num > max){
                max = num;
            }
        }
        int ans = max;
        int left = 1;
        int right = max;
        int mid = 0;
        int hours = 0;
        while(left <= right){
            mid = (right + left) / 2;
            hours = 0;
            for(int i = 0; i < piles.length; i++){
                hours+=(int) Math.ceil((double)piles[i] / mid);
            }
           
            if(hours <= h && hours > 0){
                if(mid < ans){
                    ans = mid;
                }
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return ans;
    }
}