class Solution {
public:
    string reformat(string s) {
        int n = s.length();
        char arr[n+1];
        strcpy(arr, s.c_str());
        int strCounter = 0;
        int numCounter = 0;
        int x;
        char str[n+1];
        char num[n + 1];
        int nu = 0; int st = 0;
        for (int i = 0; i < n; i++) {
            if ((int) arr[i] <= 57 && (int) arr[i] >=48) {
                numCounter++;
                num[nu] = arr[i];
                nu++;
            } else {
                strCounter++;
                str[st] = arr[i];
                st++;
            }
        }
        if ((numCounter > strCounter + 1) || (strCounter > numCounter + 1)) {
            return "";
        } else {
            string ns = "";
            if (numCounter > strCounter) {
                for (int i = 0; i < numCounter; i++) {
                    if (i == numCounter - 1) {
                        ns += num[i];
                    } else {
                        ns += num[i];
                        ns += str[i];
                    }
                }
                return ns;
            } else if (numCounter == strCounter) {
                for (int i = 0; i < numCounter; i++) {
                    ns += num[i];
                    ns += str[i];
                }
                return ns;
            } else {
                for (int i = 0; i < strCounter; i++) {
                    if (i == strCounter -1) {
                        ns += str[i];
                    } else {
                        ns += str[i];
                        ns+= num[i];
                    }
                }
            }
            return ns;
        }
    }
};