class Solution {
public:
    bool isSelfDividing(int x) {
        for (int i=x;i>0;i/=10) {
            if (!(i%10) || (x % (i%10))) {
                return false;
            }
        }
        return true;
    }
    
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int>ans;
        for (int i=left;i<=right;i++) {
            if (isSelfDividing(i)) {
                ans.push_back(i);
            }
        }
        return ans;
    }
};