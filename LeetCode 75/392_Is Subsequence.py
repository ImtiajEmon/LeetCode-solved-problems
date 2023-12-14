class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 1:
            if s in t:
                return True
            return False

        index = 0
        arr = []
        for char in s:
            while index < len(t):
                if char == t[index]:
                    arr.append(char)
                    index += 1
                    break
                index += 1
        
        return len(arr) == len(s)
