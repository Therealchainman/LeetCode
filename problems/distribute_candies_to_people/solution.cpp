class Solution {
public:
    vector<int> distributeCandies(int c, int n) {
        int prev=0;
        vector<int> res(n,0);
        for (int i=0; c>0;i++) {
            prev++;
            res[i%n]+=min(prev,c);
            c-=prev;
        }
        return res;
    }
};