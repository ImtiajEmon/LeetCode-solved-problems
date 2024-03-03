class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        digitToChar = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        def combination(com_str, i):
            if len(com_str) == len(digits):
                ans.append(com_str)
                return

            for c in digitToChar[digits[i]]:
                #com_str += c
                combination(com_str + c, i+1)

        if digits:
            combination("", 0)

        return ans
