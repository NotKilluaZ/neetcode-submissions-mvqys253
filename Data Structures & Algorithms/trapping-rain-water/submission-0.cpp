class Solution {
public:
    int trap(vector<int>& height) {
        if(height.empty()){
            return 0;
        }
        int right = height.size();
        int res = 0;

        for(int left = 0; left < right; left++){
            int leftMax = height[left];
            int rightMax = height[left];

            for(int i = 0; i < left; i++){
                leftMax = max(leftMax, height[i]);
            }
            for(int i = left + 1; i < right; i++){
                rightMax = max(rightMax, height[i]);
            }

            res += min(leftMax, rightMax) - height[left];
        }
        return res;
    }
};
