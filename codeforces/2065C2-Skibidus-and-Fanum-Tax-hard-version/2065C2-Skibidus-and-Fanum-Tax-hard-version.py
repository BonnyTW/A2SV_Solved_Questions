from bisect import bisect_left

t = int(input())

for _ in range(t):
    n,m=[int(ch) for ch in input().split()]

    a=[int(ch) for ch in input().split()]
    b=[int(ch) for ch in input().split()]

    b.sort()
    
    prev = min(a[0],b[0] - a[0])

    for i in range(1,n):
        idx = bisect_left(b , prev + a[i])

        if idx == m and a[i] < prev:
            print('NO')
            break

        elif idx == m:
            prev = a[i]
        
        else:
            if a[i] < prev:
                prev = b[idx] - a[i]
            else:
                prev = min (b[idx] - a[i],a[i])
    else:
        print("YES")