class Solution {
public:
    string makeGood(string s) {
        vector <char> stk;
        for (int i=0;i<s.length();i++) {
            stk.push_back(s[i]);
            while (stk.size() >= 2 && stk.at(stk.size()-1) != stk.at(stk.size()-2) 
                   && tolower(stk.at(stk.size()-1)) == tolower(stk.at(stk.size()-2))) {
                stk.pop_back();
                stk.pop_back();
            }
        }
        ostringstream res;
        copy(stk.begin(), stk.end(),ostream_iterator<char>(res,""));
        return res.str();
    }
};