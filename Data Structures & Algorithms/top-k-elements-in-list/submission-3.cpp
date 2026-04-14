class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        map<int, int> freqTab;

        for(int i = 0; i < nums.size(); i++){
            freqTab[nums[i]]++;
        }

        while(res.size() < k){
            int highFreq = -1;
            int highNum;
            for(auto& [num, freq] : freqTab){
                if(freq > highFreq){
                    highFreq = freq;
                    highNum = num;
                }
            }
            res.push_back(highNum);
            freqTab.erase(highNum);
        }
        return res;
    }
};
