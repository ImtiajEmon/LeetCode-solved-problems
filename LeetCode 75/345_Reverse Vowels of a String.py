class Solution:
    def reverseVowels(self, s: str) -> str:
        flag1 = False
        flag2 = False
        i, j = 0,  len(s)-1
        str_arr = [0] * (len(s))
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while i <= j:
            if s[i] in vowels:
                flag1 = True
            else:
                str_arr[i] = s[i]
                i += 1
                flag1 = False

            if s[j] in vowels:
                flag2 = True
            else:
                str_arr[j] = s[j]
                j -= 1
                flag2 = False

            if flag1 and flag2:
                str_arr[i] = s[j]
                str_arr[j] = s[i]
                i += 1
                j -= 1

        ans = ''
        for i in str_arr:
            ans += i
        return ans
