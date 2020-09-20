class Solution:
    def reorderSpaces(self, text):
        num_spaces = text.count(" ")
        A = text.split()
        n = len(A)
        if n == 1:
            return A[0] + " " * num_spaces
        spaces_between = num_spaces // (n - 1)
        spaces_remain = num_spaces % (n - 1)
        return (" "*spaces_between).join(A) + " "*spaces_remain
        