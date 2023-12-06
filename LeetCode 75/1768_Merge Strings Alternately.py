class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        i = 0
        while i < len(word1) and i < len(word2):
            merged_string += word1[i] + word2[i]
            i += 1

        merged_string += word1[i:]
        merged_string += word2[i:]

        return merged_string
