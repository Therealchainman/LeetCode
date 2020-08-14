class Solution {
public:
    int longestPalindrome(string s) {
        int odd=0;
        set <char>H (s.begin(), s.end());
        for (auto e: H) {
            int c = count(s.begin(),s.end(),e);
            if (c%2!=0) {
                odd++;
            }
        }
        return odd>0 ? s.length() - odd + 1 : s.length();
    }
};