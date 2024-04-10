import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    String[] keywords_balance = { "balance", "balance"};

    /*
     * Complete the 'getMinFlips' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING pwd as parameter.
     */

    public static int getMinFlips(String pwd) {
    // Write your code here
    // going to try greedy algorithm
    
        char current_char = pwd.charAt(0);
        int even_count = 1;
        int flips = 0;
        
        for(int i = 1; i < pwd.length(); i++){
            if(current_char != pwd.charAt(i)){
                if(even_count % 2 == 0){    // if at even then move to next character
                    current_char = pwd.charAt(i);
                    even_count = 1;
                }
                else{   // flip char to be same as currect char
                    flips++;  
                    even_count++;  
                }
            }
            else{   // if current_char == char we're looking at
                    even_count++;
            }
        
        
        }
    return flips;

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String pwd = bufferedReader.readLine();

        int result = Result.getMinFlips(pwd);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
}