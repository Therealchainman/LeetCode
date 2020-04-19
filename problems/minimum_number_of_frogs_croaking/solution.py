class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        n = len(croakOfFrogs)
        ongoing, maxOngoing = 0, 0
        states = {k : 0 for k in range(5)}
        for ch in croakOfFrogs:
            index = "croak".index(ch)
            if (index == 0):
                ongoing += 1
                maxOngoing = max(maxOngoing, ongoing)
                states[index] += 1
            elif (index > 0 and index < 4):
                if (states[index-1] > 0):
                    states[index - 1] -= 1
                    states[index] += 1
                else:
                    return -1
            elif (index == 4):
                if (states[3] > 0):
                    states[3] -= 1
                    ongoing -= 1
                else:
                    return -1
        if sum([states[k] for k in range(4)]) > 0:
            return -1
        else:
            return maxOngoing