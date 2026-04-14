class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res(2);
        for(int left = 0; left < numbers.size(); left++){
            for(int right = left + 1; right < numbers.size(); right++){
                if(numbers[left] + numbers[right] == target){
                    res[0] = left + 1;
                    res[1] = right + 1;
                    return res;
                }
            }
       }
    }
};
