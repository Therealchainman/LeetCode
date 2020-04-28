from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @functools.lru_cache(maxsize = None)
        def memoize(pointer1: int, pointer2: int) -> int:
            
            if pointer1 == len(text1) or pointer2 == len(text2):
                return 0
            if text1[pointer1] == text2[pointer2]:
                return memoize(pointer1 + 1, pointer2 + 1) + 1
            else:
                return max(memoize(pointer1+1,pointer2), memoize(pointer1, pointer2+1))
        return memoize(0,0)