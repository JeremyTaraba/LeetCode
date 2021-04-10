class Solution {
public:
    string truncateSentence(string s, int k) {
        string sentence;
        int numSpaces = 0;
        int lastIndex = 0;
        int i;
        for(i = 0; i < s.size(); i++){
            if(numSpaces >= k){
                cout << "breaking" << endl;
                break;
            }
            if(s.at(i) == ' '){
                numSpaces++;
                sentence.append(s, lastIndex, i-lastIndex);
                cout << "sentence = " << sentence << endl;
                lastIndex = i;
            }
        }
        if(i == s.size()){
            sentence = s;
        }
        
        return sentence;
    }
};