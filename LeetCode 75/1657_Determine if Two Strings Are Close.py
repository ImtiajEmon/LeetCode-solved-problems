class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = dict()
        dict2 =  dict()

        for i in word1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in word2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1

        myKeys1 = list(dict1.keys())
        myKeys1.sort()
        freq1 = [dict1[i] for i in myKeys1]
        freq1.sort()

        myKeys2 = list(dict2.keys())
        myKeys2.sort()
        freq2 = [dict2[i] for i in myKeys2]
        freq2.sort()

        if myKeys1 == myKeys2 and freq1 == freq2:
            return True
        else:
            return False
        
