class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeats = []
        count = 0
        chars = list(s)
        temp = 0
        i = 0
        start = 0
        if len(s) == 0:
            return 0
        while i < len(s):
            if chars[i] in repeats:
                count = max(len(repeats), count)
                repeats.remove(repeats[start])

            else:
                repeats.append(s[i])
                i += 1
        if len(s) > 0:
            count = max(len(repeats), count)
        return count


stringer = "abcabcbb"
s = Solution()
print(s.lengthOfLongestSubstring(stringer))
