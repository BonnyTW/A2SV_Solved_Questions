class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        initial=float('inf')
        ans=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                i_list2=list2.index(list1[i])
                tot=i+i_list2
                if tot<initial:
                    ans.clear()
                    ans.append(list1[i])
                    initial=tot
                elif tot==initial:
                    ans.append(list1[i])
                else:
                    continue
        return ans
         
