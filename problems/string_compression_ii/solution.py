class Solution:
    def getLengthOfOptimalCompression(self, s, k):
        n = len(s)
        inf = float('inf')
        
        def rle(x):
            # the length of a RLE-version of
            # a character repeated x times.
            if x <= 1:
                return x
            if x <= 9:
                return 2
            if x <= 99:
                return 3
            return 4
        
        @lru_cache(None)
        def dp(i, eaten):
            if eaten > k:
                return inf
            if i == n:
                return 0
            
            length = deleted = 0
            ans = dp(i+1,eaten+1)
            for j in range(i, n):
                if s[i] == s[j]:
                    length += 1
                else:
                    deleted += 1
                ans = min(ans, dp(j+1, eaten+deleted) + rle(length))
            return ans
        return dp(0, 0)
        
#         @lru_cache(None)
#         def dp(i, last_char, cur_length, eaten):
#             # the minimum length of a RLE version of s[i:], where :
#             # the last characcter written was last_char
#             # the length of the suffix group of last_car is cur_length
#             # The number of characters removed currently is eaten
#             if eaten > k:
#                 return inf
#             if i == n:
#                 return 0
#             ans = dp(i + 1, last_char, cur_length, eaten + 1)
#             if s[i] == last_char:
#                 delta = rle(cur_length + 1) - rle(cur_length)
#                 dp(i + 1, s[i], cur_length + 1, eaten) + delta
#                 ans = min(ans, cand)
#             else:
#                 delta = 1
#                 cand = dp(i + 1, s[i], 1, eaten) + delta
#                 ans = min(ans, cand)
                
#             return ans
        
#         return dp(0, '', 0, 0)

