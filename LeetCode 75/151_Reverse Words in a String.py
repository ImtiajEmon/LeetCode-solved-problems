class Solution:
    def reverseWords(self, s: str) -> str:
        str_arr = s.split()
        str_arr.reverse()

        ans = ''
        for i in range(len(str_arr)):
            if i == len(str_arr)-1:
                ans += str_arr[i]
            else:
                ans += str_arr[i] + ' ' 
        return ans
