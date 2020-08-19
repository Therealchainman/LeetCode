class Solution {
public:
    vector<int> numsSameConsecDiff(int N, int K) {
        vector<int>A={0,1,2,3,4,5,6,7,8,9};
        for (int i=0;i<N-1;i++) {
            vector<int>cur;
            for (int x:A) {
                int y=x%10;
                if (x>0 && y+K<10) {
                    cur.push_back(x*10 + y+K);
                }
                if (x>0 && K>0 && y-K>=0) {
                    cur.push_back(x*10 + y-K);
                }
            }
            A=cur;
        }
        return A;
    }
};