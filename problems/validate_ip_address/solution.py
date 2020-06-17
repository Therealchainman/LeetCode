import re
class Solution:
    def validIPAddress(self, IP):
        regIPv4 = "^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$"
        regIPv6 = "^(?:(?:[0-9a-fA-F]{1,4})\:){7}(?:[0-9a-fA-F]{1,4})$"
        if re.search(regIPv4, IP): 
            return "IPv4"
        if re.search(regIPv6, IP):
            return "IPv6"
        return "Neither"
        
"""
Start time: 9:20PM
approach1:  

Conditions:
is it IPv4 or IPv6 or neither

Check if it is a valid IPv4 first
1) 4 numbers (make sure they are decimal numbers), 3 decimal points
2) no leading zeros
3) each number within range 0 <= num <= 255
4) return "IPv4"

Check if it is valid IPv6
1) 8 hexadecimal numbers (make sure they are hexadecimals, 0-9, a-f)
2) Exactly 1 to 4 digits in each hexadecimal number (group)
3) return "IPv6"

if both these fail return "neither"
"""