class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1)!=set(word2):
            return False

        count_word1=Counter(word1)
        count_word2=Counter(word2)

        countw1=list(count_word1.values())
        countw2=list(count_word2.values())
        countw1.sort()
        countw2.sort()
        for i in range (len(countw1)):
            if countw1[i]!=countw2[i]:
                return False
        return True

        
