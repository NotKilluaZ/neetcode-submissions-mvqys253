class Solution {
public:
    int bi_search(vector<int>& nums, int left, int right, int target) {
        if(left > right){
            return -1;
        }

        int mid = (right + left) / 2;
        if(nums[mid] == target){
            return mid;
        }else if(nums[mid] < target){
            return bi_search(nums, mid + 1, right, target);
        }else{
            return bi_search(nums, left, right - 1, target);
        }
    }

    int search(vector<int>& nums, int target) {
        return bi_search(nums, 0, nums.size() - 1, target);
    }
};
