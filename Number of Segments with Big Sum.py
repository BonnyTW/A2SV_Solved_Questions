n,s=[int(ch) for ch in input().split()]
arr=[int(ch) for ch in input().split()]

left=0
right=0
count=0
csum=0
while right<n:
    csum+=arr[right]

    while csum >= s:
        csum-=arr[left]
        left+=1
        count+=(n-right)
    right+=1

print( count)


