from collections import Counter
n,k=[int(ch) for ch in input().split()]
arr=[int(ch) for ch in input().split()]

left=0
right=0
count=0

distinict=Counter()

while right < n:
    distinict[arr[right]]+=1

    while len(distinict)>k:
        distinict[arr[left]]-=1
        if distinict[arr[left]]==0:
            del distinict[arr[left]]
        left+=1
    count+=right-left+1
    right+=1
print(count)
