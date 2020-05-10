class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = set(target)
        stack = []
        counter = 0
        for i in range(1, n + 1):
            if i in s:
                stack.append("Push")
                counter += 1
            else:
                stack.append("Push")
                stack.append("Pop")
            if counter == len(target):
                return stack
        return stack