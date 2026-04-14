class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        } else if(nums.size() == 1){
            return 1;
        }

        sort(nums.begin(), nums.end());

        int res = 0;
        int curr = nums[0];
        int max = 0;
        int i = 0;

        while(i < nums.size()){
            if(curr != nums[i]){
                curr = nums[i];
                max = 0;
            }
            while(i < nums.size() && nums[i] == curr){
                i++;
            }
            max++;
            curr++;
            if(res < max){
                res = max;
            }
        }
        return res;
    }
};
