class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []

        for i in range(len(queries)):
            q_word = queries[i]
            for j in range(len(dictionary)):
                count = 0
                d_word = dictionary[j]
                
                k = 0 

                while k < len(q_word):
                    if q_word[k] != d_word[k]:
                        count += 1
                    k += 1
                if count <= 2:
                    ans.append(q_word)
                    break
        return ans



        