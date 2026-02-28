n,k=[int(ch) for ch in input().split()]
arr=[int(ch) for ch in input().split()]

left=0
right=0

counted={}
maxlen=0
index=[]

while right < n:

    if arr[right] in counted:
        counted[arr[right]]+=1
    else:
        counted[arr[right]]=1
    while len(counted)>k:
        counted[arr[left]]-=1
        if counted[arr[left]]==0:
            del counted[arr[left]]
        left+=1

    curr=right-left+1

    if curr>maxlen:
        maxlen=curr
        index=[left+1,right+1]
    right+=1

print(*index)
    
    


