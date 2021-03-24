/* Prompt:

Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.


*/

#include <vector>

using namespace std;

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        int candyTypeSize = candyType.size();
        if(candyTypeSize <= 1){
            return 0;
        }
        
        int halfCandies = candyType.size() / 2;
        vector<int> chosenCandies;  //keeps track of how many candies we are allowed to eat
        int chosenCandiesSize = 1;
        int currentCandyCounter = 1;
        bool alreadyHaveCandy = false;
        
        chosenCandies.push_back(candyType.at(0));
        
        while( (chosenCandiesSize < halfCandies) && (currentCandyCounter < candyTypeSize) ){
            for(int i = 0; i < chosenCandiesSize; i++){
                if(candyType.at(currentCandyCounter) == chosenCandies.at(i)){
                    alreadyHaveCandy = true;
                    break;
                }
            }
            if(!alreadyHaveCandy){
                chosenCandies.push_back(candyType.at(currentCandyCounter));
            }
            
            alreadyHaveCandy = false;
            chosenCandiesSize = chosenCandies.size();
            currentCandyCounter++;
        }
        
        return chosenCandiesSize;
    }
};

/*
notes: If candyType is always ordered then we can just use an int to keep track of how many candies we are allowed to eat.
We could also just store the chosen candies inside of the vector candyType and remove and repeating candy types and any types that go beyond the max amount of candies we can eat. This only works if we are allowed to manipulate the original vector since it is passed by reference.

*/