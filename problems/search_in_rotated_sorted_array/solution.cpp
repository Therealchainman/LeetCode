class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if (n == 0) {
            return -1;
        } else if (n == 1) {
            if (nums[0] == target) {
                return 0;
            } else {
                return -1;
            }
        }
        if (nums[0] > target) {
            for (int i = n - 1; i > 0; i--){
                cout << i << endl;
                if (nums[i] == target) {
                    return i;
                } else if (nums[i] < target) {
                    return -1;
                }
            }
            return -1;
        } else {
            for (int i = 0; i < n; i++){
                if (nums[i] == target) {
                    return i;
                } else if (nums[i] > target) {
                    return -1;
                }
            }
            return -1;
        }
        return 0;
    }
};