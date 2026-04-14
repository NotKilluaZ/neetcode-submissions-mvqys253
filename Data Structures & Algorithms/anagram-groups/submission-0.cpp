class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        if(strs.size() < 2){
            res.push_back(strs);
            return res;
        }

        while(strs.size() != 0){
            string first = strs[0];
            strs.erase(strs.begin());
            vector<string> temp;
            temp.push_back(first);
            for(int i = strs.size() - 1; i >= 0; i--){
                string firstCopy = first;
                sort(firstCopy.begin(), firstCopy.end());
                string strCopy = strs[i];
                sort(strCopy.begin(), strCopy.end());
                if(firstCopy == strCopy){
                    temp.push_back(strs[i]);
                    strs.erase(strs.begin() + i);
                }
            }
            res.push_back(temp);
        }
        return res;
    }
};
