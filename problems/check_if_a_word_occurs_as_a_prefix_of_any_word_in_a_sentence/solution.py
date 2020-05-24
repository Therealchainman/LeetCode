class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split()
        res = -1
        for j in range(len(l)):
            if len(l[j]) >= len(searchWord):
                flag = True
                for i in range(len(searchWord)):
                    if l[j][i] != searchWord[i]:
                        flag = False
                        break
                if flag:
                    return j + 1
        return res