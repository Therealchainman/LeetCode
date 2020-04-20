class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        while (1) {
            int m = (r + l) >> 1;
            if (nums[m] == target) {
                return m;
            } 
            if (m == l && m ==r)  {
                return -1;
            }
            if (target < nums[m]) {
                r = max(m - 1, 0);
            } else {
                l = m + 1;
            }
        }
    }
};