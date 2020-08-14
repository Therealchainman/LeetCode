class CombinationIterator {
    
    
public:
    vector<int> p;
    string c;
    int f=0;
    int l,n;
    CombinationIterator(string characters, int combinationLength) {
        c=characters;
        l=characters.length();
        n=combinationLength;
        for (int i=0;i<n;i++) p.push_back(i);
    }
    
    string next() {
        string res ="";
        if (f==0) {
            for (int i=0;i<n;i++){
                res+=c[p[i]];
                f=1;
            }
            return res;
        }
        for (int i=n-1;i>-1;i--) {
            if (p[i]!=i+l-n){
                p[i]++;
                for (int j=i+1;j<n;j++) {
                    p[j]=p[i]+j-i;
                }
                break;
            }
        }
        for (int i=0;i<n;i++){
            res+=c[p[i]];
        }
        return res;
    }
    
    bool hasNext() {
        return p[0]!=l-n;
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */