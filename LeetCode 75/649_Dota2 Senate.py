class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        def do_round(s):
            d = 0
            r = 0
            new_s = ''

            for i in s:
                if i == 'D':
                    if r > 0:
                        r -= 1
                    else:
                        new_s += i
                        d += 1
                else:
                    if d > 0:
                        d -= 1
                    else:
                        new_s += i
                        r += 1
            if d > 0:
                i = 0
                while i < len(new_s):
                    if new_s[i] == 'R' and d > 0:
                        new_s = new_s[:i] + new_s[i+1:]
                        d -= 1
                    else:
                        i += 1
            
            if r > 0:
                i = 0
                while i < len(new_s):
                    if new_s[i] == 'D' and r > 0:
                        new_s = new_s[:i] + new_s[i+1:]
                        r -= 1
                    else:
                        i += 1
                
            return new_s

        while True:
            if senate[0] * len(senate) == senate:
                if senate[0] == 'R':
                    return 'Radiant'
                else:
                    return 'Dire'

            senate = do_round(senate)
