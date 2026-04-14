class MinStack {
public:
    MinStack() {
    
    }
    
    void push(int val) {
        st.push(val);
        if(min.empty() || val <= min.top()){
            min.push(val);
        }
    }
    
    void pop() {
        if(min.top() == st.top()){
            min.pop();
        }
        st.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return min.top();
    }

private:
    stack<int> st;
    stack<int> min;
};
