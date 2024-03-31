class Solution {
    public boolean isAnagram(String s, String t) {
        // adding to a single map then decrement map based on t and check if values are all 0
        if(s.equals(t)){
            return true;
        }
        if(s.length() != t.length()){
            return false;
        }
        int length = s.length();
        Map<Character, Integer> sMap = new HashMap<>();
        for(int i = 0; i < length; i++){
            sMap.merge(s.charAt(i), 1, Integer::sum);
        }
        
        for(int i = 0; i < length; i++){
            sMap.merge(t.charAt(i), -1, Integer::sum);
        }

        for (int i : sMap.values()){
            if(i != 0){
                return false;
            }
        }


        return true;
    }
}