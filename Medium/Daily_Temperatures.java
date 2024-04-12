class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        // could compare every i with the rest of the list. Worst case is O(n^2)
        // can do better if we use more storage. O(n) storage using a stack and O(n) time 
        Stack<Pair<Integer, Integer>> stackTemps = new Stack<>();
        int[] ans = new int[temperatures.length];
        

        for(int i = 0; i < temperatures.length; i++){
           while (!stackTemps.isEmpty() && temperatures[i] > stackTemps.peek().getValue()){
                Pair<Integer, Integer> temp = stackTemps.pop();
                ans[temp.getKey()] = i - temp.getKey();
           }
           Pair<Integer, Integer> p = new Pair<>(i,temperatures[i]);
           stackTemps.push(p);
        }


        return ans;
    }
}