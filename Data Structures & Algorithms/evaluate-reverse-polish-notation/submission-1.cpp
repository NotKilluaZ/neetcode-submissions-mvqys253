class Solution {
public:
    int evalRPN(vector<string>& tokens) {
         stack<int> nums;
         for(auto& token : tokens){
            if(token != "+" && token != "-" && token != "*" && token != "/"){
                nums.push(stoi(token));
            }else{
                int num1 = nums.top();
                nums.pop();
                int num2 = nums.top();
                nums.pop();
                int endNum;
                if(token == "+"){
                    endNum = num1 + num2;
                }else if(token == "-"){
                    endNum = num2 - num1;
                }else if(token == "*"){
                    endNum = num1 * num2;
                }else if(token == "/"){
                    endNum = num2 / num1;
                }
                nums.push(endNum);
            }
         }
         return nums.top();
    }
};
