class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        flag = False

        for i in range(len(word)):
            if word[i] == ch:
                flag = True
                break

        if flag:
            new_str = word[i : : -1]
            new_str += word[i+1 : :]
        else:
            new_str = word

        return new_str
        
