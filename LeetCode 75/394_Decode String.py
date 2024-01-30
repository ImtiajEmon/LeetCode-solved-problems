#Implementing Stack with list
class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()

        def make_string():
            st = ''
            temp = ''
            while temp != '[':
                st = temp + st
                temp = stack.pop()

            k = stack.pop()
            st = k*st
            stack.append(st)
        
        prev_digit = False
        for char in s:
            if char == ']':
                make_string()

            elif char.isdigit():
                if prev_digit:
                    temp = str(stack.pop()) + char
                    stack.append(int(temp))
                else:
                    stack.append(int(char))
                    prev_digit = True
            
            else:
                stack.append(char)
                prev_digit = False

        ans = ''
        while len(stack) != 0:
            ans = stack.pop() + ans
        return ans
