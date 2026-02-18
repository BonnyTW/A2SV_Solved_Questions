class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arrv1=[int (ch) for ch in version1.split('.')]
        arrv2=[int (ch) for ch in version2.split('.')]
        

        if len(arrv1)!=len(arrv2):
            if len(arrv2)>len(arrv1):
                arrv1=arrv1+[0]*(len(arrv2)-len(arrv1))
            else:
                arrv2=arrv2+[0]*(len(arrv1)-len(arrv2))
        print(arrv1)
        print(arrv2)

        i=0
        j=0

        flagv1=False
        flagv2=False
        while i <len(arrv1) and j<len(arrv2):
            if arrv1[i]>arrv2[j]:
                flagv1=True
                break
            elif arrv1[i]<arrv2[j]:
                flagv2=True
                break
            i+=1
            j+=1
        
        if flagv1:
            return 1
        elif flagv2:
            return -1
        else:
            return 0

        
