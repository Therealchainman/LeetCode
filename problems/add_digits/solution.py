class Solution:
    def addDigits(self, num: int) -> int:
        # Using the digital root 
        if num == 0:
            return 0 
        
        rem = num % 9
        return rem if rem != 0 else 9
        
        
        
        # numS = str(num)
        # while len(numS) > 1:
        #     localSum = 0
        #     for n in numS:
        #         localSum += int(n)
        #     numS = str(localSum)
        # return int(numS)
        