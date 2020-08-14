class Solution {
public:
    char findKthBit(int n, int k) {
        vector<int> A {0};
        while (k>=A.size()) {
            A.push_back(1);
            for (int i=A.size()-2;i>-1;i--) {
                A.push_back(A[i]^1);
            }
        }
        char c = A[k-1]+'0';
        return c;  
    }
};