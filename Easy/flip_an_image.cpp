#include <stack>

using namespace std;

// takes in a vector of a vector of integers and reverses the order of bits
// then it flips the bits after reversing it.
// aka 0's become 1's and 1's become 0's

class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        stack<int> horizontal_flip;
        for(int i = 0; i < A.size(); i++){
            for(int j = 0; j < A.at(i).size(); j++){
                horizontal_flip.push(A.at(i).at(j));
            }
            A.at(i).clear();
            int size_of = horizontal_flip.size();
            for(int k = 0; k < size_of; k++){
                if(horizontal_flip.top() == 0){
                    A.at(i).push_back(1);
                }
                else{
                    A.at(i).push_back(0);
                }
                horizontal_flip.pop();
            }
        }
        
        return A;
    }
};