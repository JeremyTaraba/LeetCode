class Solution {
    public String frequencyString(String s){
        int[] count = new int[26];
        for(char c : s.toCharArray()){
            count[c - 'a'] += 1;
        }

        StringBuilder frequency = new StringBuilder();
        for(int i = 0; i < 26; i++){
            if(count[i] != 0){
                frequency.append((char) ('a'+i)).append(count[i]);
            }
        }
        return frequency.toString();
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        // imagine its ints and you want to group same ints together
        // [1,1,1,2,1,2,3] you would make a map and put them into a map
        // key 1 : value = [1,1,1,1], key 2 : value = [2,2]
        // so for strings it gonna be
        // key tea : value [eat,tea,ate]  // how to make tea == eat == ate? can sort them? O(nlogn * n) tho
        // we will use frequency string to reduce the run time to O(n*m) where m is size of string
        // frequency string is aab = a2b1 we want also aba = a2b1 so original order doesnt matter

        List<List<String>> res = new ArrayList<List<String>>();
        Map<String, List<String>> groups = new HashMap<>();

        for(String s: strs){
            String tempFreq = frequencyString(s);
             if(groups.containsKey(tempFreq)){
                groups.get(tempFreq).add(s);
            }
            else{
                List<String> tempArrayList = new ArrayList<>();
                tempArrayList.add(s);
                groups.put(tempFreq, tempArrayList);
            }
        }

        res.addAll(groups.values());

        


        return res;
    }
}