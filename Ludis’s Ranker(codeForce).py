n = int(input())
arr=[int(ch) for ch in input().split()]
mydict={}
 
for i in range (len(arr)):
    if arr[i] not in mydict:
        mydict[arr[i]]=[i]
    else:
        mydict[arr[i]].append(i)
mydict=dict(sorted(mydict.items(),key=lambda x:x[0],reverse=True))
rank=1
for k in mydict:
    res=mydict[k]
    for n in res:
        arr[n]=rank
    rank+=len(res)
print(*arr)
