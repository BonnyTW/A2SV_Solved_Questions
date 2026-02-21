n=int(input())
arr=[int(ch) for ch in input().split()]

arr.sort()
minimal=float('inf')
point=0
i=0

while i < len(arr):
    right=len(arr)-1-i
    left=len(arr)-right-1

    right_sum=((right+1)*right)//2
    left_sum=((left+1)*left)//2

    tot=right_sum+left_sum

    if tot < minimal:
        minimal=tot
        point=arr[i]

    i+=1
print(point)




