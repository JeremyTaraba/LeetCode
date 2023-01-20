public class Solution {
    public int MySqrt(int x) {
        long y = 0;
        long i = 1;
        long ans = 0;  
       
        //every n odd numbers is a sqrt of n so using that we can solve this

        while(x >= y){
            y+= i;
            i+= 2;
            ans++;
        }

        return Convert.ToInt32(ans - 1);
    }
}