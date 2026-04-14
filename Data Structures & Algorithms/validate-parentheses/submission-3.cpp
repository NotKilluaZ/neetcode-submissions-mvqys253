class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for(auto& p : s){
            if(p == '}'){
                if(st.empty() || st.top() != '{'){
                    return false;
                }
                st.pop();
            }else if(p == ']'){
                if(st.empty() || st.top() != '['){
                    return false;
                }
                st.pop();
            }else if(p == ')'){
                if(st.empty() || st.top() != '('){
                    return false;
                }
                st.pop();
            }else{
                st.push(p);
            }
        }
        if(!st.empty()){
            return false;
        }else{
            return true;
        }
    }
};
