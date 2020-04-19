class Solution {
public:
    int minNumberOfFrogs(string croakOfFrogs) {
        int n = croakOfFrogs.length();
        int ongoing = 0, maxOngoing = 0;
        unordered_map<char, int> states = {};
        vector<int> arr = {0, 1, 2, 3, 4};
        string croak = "croak";
        for (auto ch : arr) {
            states[ch] = 0;
        }
        for (auto ch : croakOfFrogs) {
            int i = croak.find(ch);
            if (i == 0) {
                states[i] += 1;
                ++ongoing;
                maxOngoing = max(maxOngoing, ongoing);
            } else if (i > 0 && i < 4) {
                if (states[i - 1] > 0) {
                    states[i - 1]--;
                    states[i]++;
                } else {
                    return -1;
                }
            } else if (i == 4) {
                if (states[i - 1] > 0) {
                    states[i - 1]--;
                    states[i]++;
                    --ongoing;
                } else {
                    return -1;
                }
            }
        }
        for (auto i : arr) {
            if (i != 4 && states[i] > 0) {
                return -1;
            } 
            }
        return maxOngoing;
        }
};