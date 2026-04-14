class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> compare;
        for(int i = 0; i < nums.size(); i++){
            if(compare.count(nums[i]) == 1){
                return true;
            }
            compare.insert(nums[i]);
        }
        return false;
    }
};
