class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = ""
        count = 0

        temp_count = 0
        for i in range(len(s)):
            while s[i] in sub_str:
                sub_str = sub_str[1:]
                count = max(count, temp_count)
                temp_count -= 1

            sub_str += s[i]
            temp_count += 1
        count = max(count, temp_count)
        return count
        
