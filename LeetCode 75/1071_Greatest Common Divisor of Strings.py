class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # here i decreasing the smaller str len & if the len of both str are divisible by
        #that decreasing len then we return the decreasing str
        def isEqual(ss, s1, s2):
            n1 = len(s1) // len(ss)
            n2 = len(s2) // len(ss)
            if ss*n1 == s1 and ss*n2 == s2:
                return True
            return False

        smaller_str = ''
        smaller_len = -1
        if len(str1) < len(str2):
            smaller_str = str1
            smaller_len = len(str1)
        else:
            smaller_str = str2
            smaller_len = len(str2)

        while smaller_len > 0:
            if len(str1) % smaller_len == 0 and len(str2) % smaller_len == 0:
                if isEqual(smaller_str, str1, str2):
                    return smaller_str

            smaller_str = smaller_str[:-1]
            smaller_len -= 1
        return ''

        
