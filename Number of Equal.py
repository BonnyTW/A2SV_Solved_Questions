n,m=[int(ch) for ch in input().split()]
arr1=[int(ch) for ch in input().split()]
arr2=[int(ch) for ch in input().split()]


fir=0
sec=0
count=0

while fir < n and sec < m:
    if arr1[fir] < arr2[sec]:
        fir += 1
    elif arr1[fir] > arr2[sec]:
        sec += 1
    else:
        curr=arr1[fir]
        count_arr1=0
        count_arr2=0

        while sec < m and arr2[sec]==curr:
            count_arr2+=1
            sec+=1

        while fir < n and arr1[fir]==curr:
            count_arr1+=1
            fir+=1
        
        count+=count_arr1*count_arr2

    
print(count)





