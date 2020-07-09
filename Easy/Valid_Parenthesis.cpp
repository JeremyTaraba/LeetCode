class Solution {
public: 
    bool isValid(string s) {
        stack<char> leftP;
        for(int i = 0; i < s.length(); i++){
            
            if(s.at(i) == '(' || s.at(i) == '{' || s.at(i) == '['){
                leftP.push(s.at(i));
            }
            
            else if (s.at(i) == ')' || s.at(i) == '}' || s.at(i) == ']'){
                if(leftP.empty()){
                    return false;
                }
                
                if(leftP.top() == '(' && s.at(i) == ')' ){  
                    leftP.pop();
                }
                
                else if(leftP.top() == '[' && s.at(i) == ']' ){  
                    leftP.pop();
                }
                
                else if(leftP.top() == '{' && s.at(i) == '}' ){  
                    leftP.pop();
                }
                
                else{
                    return false;
                }
            }
            
        }
        
        if(leftP.empty()){
            return true;
        }
        return false;
        
    }
};