class Solution {
public:
    int maxArea(vector<int>& heights) {
        int res = 0;
        for(int left = 0; left < heights.size(); left++){
            for(int right = left + 1; right < heights.size(); right++){
                int area = min(heights[left], heights[right]) * (right - left);
                res = max(res, area);
            }
        }
        return res;
    }
};
