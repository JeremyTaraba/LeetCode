class Solution {
    public boolean isPalindrome(String s) {
        // 2 pointer approach
        s = s.toLowerCase();
        String newS = s.replaceAll("[^A-Za-z0-9]+", "");
        System.out.println(newS);
        int left = 0;
        int right = newS.length()-1;

        while(left < right){
            if(newS.charAt(left) != newS.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}