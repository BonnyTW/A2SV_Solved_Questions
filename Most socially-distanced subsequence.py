t=int(input())

for _ in range(t):
    n=int(input())
    arr=[int(ch) for ch in input().split()]

    ans=[arr[0]]

    for i in range(1,n):
        if i<n-1:
            if arr[i-1] < arr[i] > arr[i+1] or arr[i-1] > arr[i] < arr[i+1]:
                ans.append(arr[i])
    ans.append(arr[-1])

    print(len(ans))
    print(*ans)
