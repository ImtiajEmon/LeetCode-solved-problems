class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        num_of_vowel = 0
        max_num_of_vowel = 0

        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(k):
            if s[i] in vowels:
                num_of_vowel += 1

        max_num_of_vowel = num_of_vowel
        for i in range(k, len(s)):
            if s[i] in vowels:
                num_of_vowel += 1
            if s[i-k] in vowels:
                num_of_vowel -= 1
            max_num_of_vowel = max(max_num_of_vowel, num_of_vowel)

        return max_num_of_vowel
        
