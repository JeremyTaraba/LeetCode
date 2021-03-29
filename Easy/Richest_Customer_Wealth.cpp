/*
Prompt:
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Example:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.


*/


class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        short int maxWealth = 0;
        short int tempWealth = 0;
        for(char i = 0; i < accounts.size(); i++){
            for(char j = 0; j < accounts.at(i).size(); j++){
                tempWealth += accounts.at(i).at(j);
            }
            if(tempWealth > maxWealth){
                maxWealth = tempWealth;
            }
            tempWealth = 0;
        }
        
        
        return maxWealth;
    }
};



/*
Notes:
use smaller datatypes to save on size

Contraints:
m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100

maxWealth will be between 1 < 50*100 
can use char or unsigned char for the size of the vectors

*/