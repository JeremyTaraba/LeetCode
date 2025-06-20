public class Solution {
    public bool DivideArray(int[] nums) {
        // check for even number of nums (guaranteed so don't need to check)
        // then check how many nums there are by using a map (all values should be even)
        Dictionary<int, int> dict = new Dictionary<int, int>();
        foreach(int n in nums){
            dict.TryGetValue(n, out var currentCount);
            dict[n] = currentCount+1;
        }

        foreach(var item in dict){
            if(item.Value % 2 != 0){
                return false;
            }
        }


        // return true if so
        return true;
    }
}