class Solution:
    def reverse(self, x):
        overflow=2**31
        if x<0:
            s=str(x)[1:]
            x=-int(s[::-1])
        else:
            x=int(str(x)[::-1])
        return x if -overflow<=x<overflow else 0
        