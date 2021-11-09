/*
Prompt:
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

*/


class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int value = 0;
        for(String x:operations){
            if(x.charAt(1) == '+'){
                value++;
            }
            else{
                value--;
            }
        }
        
        return value;
    }
}

/*
Notes:
We only need to check the character in the middle of the string since it 
will always be a + or -


Constraints:
1 <= operations.length <= 100
operations[i] will be either "++X", "X++", "--X", or "X--".

*/