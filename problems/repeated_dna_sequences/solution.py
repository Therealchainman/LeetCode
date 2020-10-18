class Solution:
    def findRepeatedDnaSequences(self, s):
        r, record = set(), set()
        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in record:
                r.add(substring)
            record.add(substring)
        return list(r)
        