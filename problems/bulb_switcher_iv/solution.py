class Solution:
    def minFlips(self, target: str) -> int:
        groups = 0
        prev = "-1"
        for i in range(len(target)):
            if target[i] == "1" and prev != "1":
                groups += 1
                prev = target[i]
            if target[i] == "0" and prev == "1":
                groups += 1
                prev = target[i]
        return groups