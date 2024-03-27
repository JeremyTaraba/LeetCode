import java.util.*;

public class Contains_Duplicate {
    public static void main(String[] args) {
        int nums[] = {1,2,3,4,5,6};
        Dictionary<Integer, Integer> dict = new Hashtable<>();

        // If the key is new then null is returned, otherwise it returns the old key and replaces it

        for(int i : nums){
            Integer temp = dict.put(i, 1);  //int cannot be null, Integer can be null
            if(temp != null){
                System.out.println("true");
            }
        }

        System.out.println("false");
    }
}
