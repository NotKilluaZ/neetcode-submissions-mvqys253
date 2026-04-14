class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res = {0, 1};
        for(int left = 0; left < nums.size() - 1; left++){
            for(int right = 1; right < nums.size(); right++){
                if(nums[left] + nums[right] == target && left != right){
                    res[0] = left;
                    res[1] = right;
                    return res;
                }
            }
        }
    }
};
