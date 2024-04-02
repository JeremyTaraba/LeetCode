class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // make a frequency map key = number, value = frequency O(n)  // this code is actually O(n*k) since 
        // we have to loop through the resulting frequencyList k times and worst case k=n
        // could also sort it and just pick the unique elements as shown in order O(nlogn)
        int[] ans = new int[k];
        Map<Integer, Integer> freqMap = new HashMap<>();
        Map<Integer, List<Integer>> simplifiedFreqMap = new HashMap<>();
        int highestFreq = 1;

        for(int i = 0; i < nums.length; i++){
            if(freqMap.containsKey(nums[i])){
                if(highestFreq < freqMap.get(nums[i])+1){
                    highestFreq = freqMap.get(nums[i])+1;
                }
                freqMap.put(nums[i], freqMap.get(nums[i])+1);
            }
            else{
                freqMap.put(nums[i], 1);
            }
        }

        for(Map.Entry<Integer, Integer> e : freqMap.entrySet()){
            if(simplifiedFreqMap.containsKey(e.getValue())){
                List<Integer> tempArrayList = simplifiedFreqMap.get(e.getValue());
                tempArrayList.add(e.getKey());
                simplifiedFreqMap.put(e.getValue(), tempArrayList);
            }
            else{
                List<Integer> tempArrayList = new ArrayList<>();
                tempArrayList.add(e.getKey());
                simplifiedFreqMap.put(e.getValue(), tempArrayList);
            }
        }

        while(k != 0 || highestFreq == 0){
            if(simplifiedFreqMap.containsKey(highestFreq)){
                for(Integer n : simplifiedFreqMap.get(highestFreq)){
                    k--;
                    ans[k] = n;
                }
            }
            highestFreq--;

        }
        



        return ans;
    }


    
}