class Solution {
public:
    bool containsDuplicate(vector<int>& sums) {
        map<int,int> store;
        for (auto i : sums){
            if (not store[i]){
                store[i] = 1;
            }
            else{
            return true;
            }
        }
        return false;
    }
};