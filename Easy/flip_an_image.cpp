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
                A.at(i).push_back(horizontal_flip.top());
                horizontal_flip.pop();
            }
            
             for(int j = 0; j < A.at(i).size(); j++){
                if(A.at(i).at(j) == 0){
                    A.at(i).at(j) = 1;
                }
                 else{
                     A.at(i).at(j) = 0;
                 }
            }
        }
        
        return A;
    }
};